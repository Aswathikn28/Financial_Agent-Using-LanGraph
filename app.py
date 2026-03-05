from flask import Flask, render_template, request, send_file
from financial_graph_agent import app_graph
import yfinance as yf
import json
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

last_result = {}

@app.route("/", methods=["GET", "POST"])
def home():
    global last_result

    result = None
    error = None
    chart_data = None
    risk_score = None
    ratios = None

    if request.method == "POST":
        company = request.form.get("company").upper()

        try:
            response = app_graph.invoke({"company": company})

            result = response
            last_result = result

            ticker = yf.Ticker(company)
            hist = ticker.history(period="6mo")

            # Moving average (20-day)
            hist["MA20"] = hist["Close"].rolling(window=20).mean()

            chart_data = {
                "dates": hist.index.strftime("%Y-%m-%d").tolist(),
                "prices": hist["Close"].tolist(),
                "ma20": hist["MA20"].fillna(0).tolist()
            }

            risk_map = {"Low": 30, "Medium": 60, "High": 90}
            risk_score = risk_map.get(result["risk_level"], 50)

            ratios = result["analysis"]

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error,
        chart_data=json.dumps(chart_data) if chart_data else None,
        risk_score=risk_score,
        ratios=ratios
    )


@app.route("/download-report")
def download_report():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>AI Financial Investment Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.5 * inch))

    for key, value in last_result.items():
        elements.append(Paragraph(f"<b>{key}</b>: {value}", styles["Normal"]))
        elements.append(Spacer(1, 0.3 * inch))

    doc.build(elements)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="financial_report.pdf")

if __name__ == "__main__":
    app.run(debug=True)