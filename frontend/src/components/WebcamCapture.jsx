import { useEffect, useRef, useState } from "react";
import api from "../services/api";
import WarningBox from "./WarningBox";
import StatusPanel from "./StatusPanel";
import ReportPanel from "./ReportPanel";

export default function WebcamCapture() {

  const videoRef = useRef(null);

  const canvasRef = useRef(null);

  const previousState = useRef(null);

  const [result, setResult] = useState(null);

  const [reportData, setReportData] =
    useState(null);

  const [tabWarning, setTabWarning] =
    useState(false);

  useEffect(() => {

    startCamera();

    document.addEventListener(
      "visibilitychange",
      handleTabSwitch
    );

    const interval = setInterval(() => {

      // ONLY analyze if tab active
      if (!document.hidden) {

        captureFrame();

      }

    }, 5000);

    return () => {

      clearInterval(interval);

      document.removeEventListener(
        "visibilitychange",
        handleTabSwitch
      );
    };

  }, []);

  // -------------------------
  // CAMERA
  // -------------------------

  const startCamera = async () => {

    const stream =
      await navigator.mediaDevices.getUserMedia({
        video: true
      });

    videoRef.current.srcObject = stream;
  };

  // -------------------------
  // TAB SWITCH
  // -------------------------

  const handleTabSwitch = async () => {

    if (document.hidden) {

      setTabWarning(true);

      try {

        await api.post(
          "/tab-switch"
        );

      } catch (error) {

        console.log(error);

      }
    }
  };

  // -------------------------
  // GENERATE REPORT
  // -------------------------

  const generateReport = async () => {

    try {

      const response =
        await api.get(
          "/generate-report"
        );

      setReportData(
        response.data
      );

    } catch (error) {

      console.log(error);

    }
  };

  // -------------------------
  // DRAW DETECTIONS
  // -------------------------

  const drawDetections = (detections) => {

    const canvas = canvasRef.current;

    const ctx = canvas.getContext("2d");

    canvas.width =
      videoRef.current.videoWidth;

    canvas.height =
      videoRef.current.videoHeight;

    ctx.clearRect(
      0,
      0,
      canvas.width,
      canvas.height
    );

    detections.forEach((det) => {

      // COLORS
      if (det.label === "phone") {

        ctx.strokeStyle = "red";
        ctx.fillStyle = "red";

      } else if (det.label === "person") {

        ctx.strokeStyle = "lime";
        ctx.fillStyle = "lime";

      } else if (det.label === "face") {

        ctx.strokeStyle = "blue";
        ctx.fillStyle = "blue";

      } else {

        ctx.strokeStyle = "yellow";
        ctx.fillStyle = "yellow";
      }

      // BOX
      ctx.lineWidth = 3;

      ctx.strokeRect(
        det.x1,
        det.y1,
        det.x2 - det.x1,
        det.y2 - det.y1
      );

      // LABEL
      ctx.font = "18px Arial";

      ctx.fillRect(
        det.x1,
        det.y1 - 25,
        90,
        25
      );

      ctx.fillStyle = "white";

      ctx.fillText(
        det.label,
        det.x1 + 5,
        det.y1 - 7
      );
    });
  };

  // -------------------------
  // FRAME ANALYSIS
  // -------------------------

  const captureFrame = async () => {

    const canvas =
      document.createElement("canvas");

    canvas.width =
      videoRef.current.videoWidth;

    canvas.height =
      videoRef.current.videoHeight;

    const ctx =
      canvas.getContext("2d");

    ctx.drawImage(
      videoRef.current,
      0,
      0
    );

    canvas.toBlob(async (blob) => {

      const formData =
        new FormData();

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

        const currentState = {
          phone:
            response.data.phone_detected,

          away:
            response.data.looking_away,

          people:
            response.data.multiple_people
        };

        const prev =
          previousState.current;

        const changed =
          !prev ||
          prev.phone !== currentState.phone ||
          prev.away !== currentState.away ||
          prev.people !== currentState.people;

        if (changed) {

          console.log(
            "State Changed"
          );

          setResult(
            response.data
          );

          drawDetections(
            response.data.detections
          );

          previousState.current =
            currentState;
        }

      } catch (error) {

        console.log(error);

      }

    }, "image/jpeg");
  };

  // -------------------------
  // UI
  // -------------------------

  return (

    <div style={{
      backgroundColor: "#0f172a",
      minHeight: "100vh",
      color: "white",
      padding: "30px"
    }}>

      <h1 style={{
        marginBottom: "20px",
        textAlign: "center",
        fontSize: "40px",
        fontWeight: "bold"
      }}>
        AI Interview Proctoring System
      </h1>

      <div
        style={{
          position: "relative",
          display: "flex",
          justifyContent: "center"
        }}
      >

        <video
          ref={videoRef}
          autoPlay
          playsInline
          width="600"
          height="450"
          style={{
            objectFit: "cover",
            borderRadius: "12px"
          }}
        />

        <canvas
          ref={canvasRef}
          width={600}
          height={450}
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "600px",
            height: "450px",
            pointerEvents: "none"
          }}
        />

      </div>

      <div style={{
        display: "flex",
        justifyContent: "center",
        marginTop: "20px"
      }}>

        <button
          onClick={generateReport}
          style={{
            padding: "12px 24px",
            fontSize: "16px",
            cursor: "pointer",
            borderRadius: "10px",
            border: "none",
            backgroundColor: "#2563eb",
            color: "white",
            fontWeight: "bold"
          }}
        >
          Generate AI Evaluation Report
        </button>

      </div>

      <div style={{
        marginTop: "30px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center"
      }}>

        <h2>
          Detection Result
        </h2>

        {
          tabWarning &&
          <p style={{
            color: "orange",
            fontWeight: "bold"
          }}>
            ⚠️ Tab Switching Detected
          </p>
        }

        <WarningBox result={result} />

        <StatusPanel result={result} />

        <ReportPanel
          reportData={reportData}
        />

      </div>

    </div>
  );
}