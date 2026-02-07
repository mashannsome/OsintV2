import os
import json
from datetime import datetime

REPORT_FILE = "reports/data.json"
HTML_FILE = "reports/index.html"


def save(data, category="scan"):
    os.makedirs("reports", exist_ok=True)

    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "data": data
    }

    # load data lama
    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "r") as f:
            try:
                records = json.load(f)
            except:
                records = []
    else:
        records = []

    records.append(record)

    # simpan json
    with open(REPORT_FILE, "w") as f:
        json.dump(records, f, indent=2)

    generate_html(records)


def generate_html(records):
    rows = ""
    for r in reversed(records):
        rows += f"""
        <tr>
            <td>{r['time']}</td>
            <td>{r['category']}</td>
            <td><pre>{r['data']}</pre></td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>OSINT V5 Dashboard</title>
        <style>
            body {{
                background:#0f172a;
                color:white;
                font-family:Arial;
            }}
            table {{
                width:100%;
                border-collapse:collapse;
                margin-top:20px;
            }}
            th, td {{
                border:1px solid #334155;
                padding:10px;
                text-align:left;
            }}
            th {{
                background:#1e293b;
            }}
            h1 {{
                color:#38bdf8;
            }}
        </style>
    </head>
    <body>
        <h1>OSINT V5 ULTIMATE PRO - Dashboard by Mashannsome </h1>
        <table>
            <tr>
                <th>Time</th>
                <th>Module</th>
                <th>Result</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    with open(HTML_FILE, "w") as f:
        f.write(html)
