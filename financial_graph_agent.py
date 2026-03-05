# financial_graph.py

from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
import yfinance as yf

# -----------------------------
# LLM (Only in Advisor)
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0
)

# -----------------------------
# STATE
# -----------------------------
class FinancialState(TypedDict, total=False):
    company: str
    financial_data: dict
    analysis: dict
    risk_level: str
    advice: str

# -----------------------------
# PLANNER
# -----------------------------
def planner_node(state: FinancialState):
    company = state["company"].upper()
    return {"company": company}

# -----------------------------
# DATA AGENT (REAL API)
# -----------------------------
def data_node(state: FinancialState):

    ticker_symbol = state["company"]
    ticker = yf.Ticker(ticker_symbol)

    # Get financial statements
    balance_sheet = ticker.balance_sheet
    income_statement = ticker.financials
    cash_flow = ticker.cashflow

    # Latest available column
    latest_col = balance_sheet.columns[0]

    total_debt = balance_sheet.loc["Total Debt"][latest_col]
    total_equity = balance_sheet.loc["Stockholders Equity"][latest_col]
    ebit = income_statement.loc["EBIT"][latest_col]
    interest_expense = abs(income_statement.loc["Interest Expense"][latest_col])
    free_cash_flow = cash_flow.loc["Free Cash Flow"][latest_col]

    financial_data = {
        "debt": float(total_debt),
        "equity": float(total_equity),
        "ebit": float(ebit),
        "interest_expense": float(interest_expense),
        "free_cash_flow": float(free_cash_flow)
    }

    return {"financial_data": financial_data}

# -----------------------------
# ANALYZER
# -----------------------------
def analyzer_node(state: FinancialState):

    data = state["financial_data"]

    debt_to_equity = data["debt"] / data["equity"]
    interest_coverage = data["ebit"] / data["interest_expense"]

    analysis_text = f"""
    Debt-to-Equity Ratio: {debt_to_equity:.2f}
    Interest Coverage Ratio: {interest_coverage:.2f}
    Free Cash Flow: {data['free_cash_flow']:.2f}
    """

    return {
        "analysis": {
            "debt_to_equity": debt_to_equity,
            "interest_coverage": interest_coverage,
            "free_cash_flow": data["free_cash_flow"],
            "raw_analysis": analysis_text
        }
    }

# -----------------------------
# RISK AGENT (Rule-Based)
# -----------------------------
def risk_node(state: FinancialState):

    company = state["company"]
    analysis = state["analysis"]

    debt_to_equity = analysis["debt_to_equity"]
    interest_coverage = analysis["interest_coverage"]
    free_cash_flow = analysis["free_cash_flow"]

    bluechip_companies = ["AAPL", "MSFT", "GOOGL", "AMZN"]

    if debt_to_equity > 2:
        if company in bluechip_companies and interest_coverage > 5:
            risk = "Medium"
        else:
            risk = "High"
    elif debt_to_equity <= 2 and free_cash_flow > 0:
        risk = "Low"
    else:
        risk = "Medium"

    return {"risk_level": risk}

# -----------------------------
# ADVISOR (LLM)
# -----------------------------
def advisor_node(state: FinancialState):

    company = state["company"]
    risk = state["risk_level"]
    analysis_text = state["analysis"]["raw_analysis"]

    prompt = f"""
    Company: {company}
    Risk Level: {risk}

    Financial Summary:
    {analysis_text}

    Provide final investment advice in 5 concise lines.
    """

    response = llm.invoke(prompt)

    return {"advice": response.content}

# -----------------------------
# GRAPH BUILD
# -----------------------------
builder = StateGraph(FinancialState)

builder.add_node("planner", planner_node)
builder.add_node("data", data_node)
builder.add_node("analyzer", analyzer_node)
builder.add_node("risk", risk_node)
builder.add_node("advisor", advisor_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "data")
builder.add_edge("data", "analyzer")
builder.add_edge("analyzer", "risk")
builder.add_edge("risk", "advisor")
builder.add_edge("advisor", END)

app_graph = builder.compile()