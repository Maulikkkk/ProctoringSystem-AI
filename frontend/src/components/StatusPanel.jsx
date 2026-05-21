export default function StatusPanel({ result }) {

  if (!result) return null;

  return (

    <div style={{
      marginTop: "20px",
      padding: "20px",
      border: "1px solid #ccc",
      borderRadius: "10px",
      width: "400px"
    }}>

      <h2>Live Status</h2>

      <p>
        Face:
        {result.face_detected ? " ✅" : " ❌"}
      </p>

      <p>
        People Count:
        {result.multiple_people}
      </p>

      <p>
        Phone:
        {result.phone_detected ? " 📱" : " ❌"}
      </p>

      <p>
        Looking Away:
        {result.looking_away ? " 👀" : " ❌"}
      </p>

<h3
  style={{
    color:
      result.risk_score > 70
        ? "red"
        : result.risk_score > 30
        ? "orange"
        : "green"
  }}
>
  Risk Score: {result.risk_score}
</h3>

    </div>
  );
}