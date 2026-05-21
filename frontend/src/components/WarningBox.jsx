export default function WarningBox({ result }) {

  if (!result) return null;

  return (

    <div style={{
      marginTop: "20px",
      padding: "15px",
      border: "2px solid red",
      borderRadius: "10px",
      width: "400px"
    }}>

      <h2>Warnings</h2>

      {
        result.phone_detected &&
        <p>📱 Phone Detected</p>
      }

      {
        result.multiple_people > 1 &&
        <p>👥 Multiple People Detected</p>
      }

      {
        result.looking_away &&
        <p>👀 Looking Away Detected</p>
      }

      {
        !result.face_detected &&
        <p>❌ Face Not Visible</p>
      }

      <h3>
        Risk Score: {result.risk_score}
      </h3>

    </div>
  );
}