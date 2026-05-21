export default function ReportPanel({
  reportData
}) {

  if (!reportData) return null;

  const {
    session_data,
    risk,
    report
  } = reportData;

  return (

    <div style={{
      marginTop: "30px",
      padding: "20px",
      border: "1px solid #ccc",
      borderRadius: "12px",
      width: "800px",
      backgroundColor: "#1e293b",
      color: "white",
      boxShadow: "0 0 20px rgba(0,0,0,0.3)"
    }}>

      <h1>
        AI Interview Report
      </h1>

      <hr />

      <h2>
        Risk Level:
        <span style={{
          color:
            risk.level === "High"
              ? "red"
              : risk.level === "Moderate"
              ? "orange"
              : "lime"
        }}>
          {" "}{risk.level}
        </span>
      </h2>

      <h3>
        Risk Score: {risk.score}
      </h3>

      <hr />

      <h2>Session Statistics</h2>

      <ul>

        <li>
          Phone Usage:
          {session_data.phone_count}
        </li>

        <li>
          Looking Away:
          {session_data.looking_away_count}
        </li>

        <li>
          Multiple People:
          {session_data.multiple_people_count}
        </li>

        <li>
          Tab Switches:
          {session_data.tab_switch_count}
        </li>

      </ul>

      <hr />

      <h2>LLM Analysis</h2>

      <div style={{
        whiteSpace: "pre-wrap",
        lineHeight: "1.7"
      }}>
        {report}
      </div>

    </div>
  );
}