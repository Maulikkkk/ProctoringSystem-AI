import { useEffect, useRef, useState } from "react";
import api from "../services/api";
import WarningBox from "./WarningBox";
import StatusPanel from "./StatusPanel";

export default function WebcamCapture() {

  const videoRef = useRef(null);

  const [result, setResult] = useState(null);

  useEffect(() => {

    startCamera();

    const interval = setInterval(() => {
      captureFrame();
    }, 3000);

    return () => clearInterval(interval);

  }, []);

  const startCamera = async () => {

    const stream =
      await navigator.mediaDevices.getUserMedia({
        video: true
      });

    videoRef.current.srcObject = stream;
  };

  const captureFrame = async () => {

    const canvas = document.createElement("canvas");

    canvas.width = videoRef.current.videoWidth;

    canvas.height = videoRef.current.videoHeight;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(
      videoRef.current,
      0,
      0
    );

    canvas.toBlob(async (blob) => {

      const formData = new FormData();

      formData.append(
        "file",
        blob,
        "frame.jpg"
      );

      try {

        const response =
          await api.post(
            "/analyze-frame",
            formData
          );

        console.log(response.data);

        setResult(response.data);

      } catch (error) {

        console.log(error);

      }

    }, "image/jpeg");
  };

  return (
    <div>

      <video
        ref={videoRef}
        autoPlay
        playsInline
        width="600"
      />

      <div>

        <h2>Detection Result</h2>
        <WarningBox result={result} />
        <StatusPanel result={result} />

        <pre>
          {JSON.stringify(result, null, 2)}
        </pre>

      </div>

    </div>
  );
}