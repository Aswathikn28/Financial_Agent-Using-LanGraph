# AI Financial Intelligence Dashboard

An AI-powered financial analytics web application that provides real-time stock analysis, risk assessment, technical indicators, and AI-generated investment insights.

Built using **Flask, LangGraph, LLM Agents, yFinance API, and Chart.js** with a premium fintech UI design.

---

## 📌 Features

### 📊 Financial Analytics

* Live stock price data (6 months historical)
* Moving Average overlay
* Interactive stock price chart
* Financial ratio mini-cards:

  * P/E Ratio
  * Market Cap
  * Dividend Yield
  * Risk Level

### 🤖 AI-Powered Insights

* Multi-agent architecture using LangGraph
* Risk classification (Low / Medium / High)
* AI-generated investment advice
* Real-time data integration

### 🎨 Premium UI

* Elegant fintech color palette
* Glassmorphism card design
* Smooth hover animations
* Light / Dark theme toggle
* Responsive layout

### 📈 Risk Visualization

* Semi-circular risk gauge
* Visual risk scoring system

### 📄 Reporting

* Exportable PDF investment report
* Clean formatted report layout

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* LangGraph
* OpenAI / LLM integration
* yFinance API

### Frontend

* HTML5
* CSS3 (Glassmorphism design)
* Chart.js
* JavaScript

### Data

* Real-time stock data via yFinance

---

## 📂 Project Structure

```
ai-financial-dashboard/
│
├── app.py
├── financial_graph.py
├── templates/
│   └── index.html
├── static/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-financial-dashboard.git
cd ai-financial-dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Or set via terminal:

**Windows**

```bash
setx OPENAI_API_KEY "your_api_key"
```

**Mac/Linux**

```bash
export OPENAI_API_KEY="your_api_key"
```

---

### 5️⃣ Run Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📈 Example Workflow

1. Enter stock symbol (e.g., AAPL)
2. System fetches real-time financial data
3. AI analyzes risk profile
4. Dashboard displays:

   * Stock trend chart
   * Moving average
   * Financial ratios
   * Risk gauge
   * AI advisory
5. Download PDF investment report

---

## 🎯 Use Cases

* AI + Finance portfolio project
* Demonstration of Multi-Agent Systems
* LLM + Real API Integration example
* Fintech dashboard prototype
* Resume-ready full-stack AI project

---

## 🔐 Security Notes

* API keys are stored in environment variables
* `.gitignore` prevents sensitive files from being pushed
* No credentials are exposed in code

---

## 🚀 Future Enhancements

* Portfolio tracking system
* Multiple stock comparison
* Technical indicators (RSI, MACD)
* User authentication
* Database integration
* Cloud deployment (AWS / Render / Railway)

---

## 👩‍💻 Author

Developed as an AI-powered financial analytics platform combining:

* Multi-agent orchestration
* Real-time market data
* Elegant fintech UI design

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to fork or contribute!

---

**Built with Intelligence. Designed with Elegance.**
