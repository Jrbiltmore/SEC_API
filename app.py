
# /app.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010129

from flask import Flask, jsonify
from api.edgar_parser import EdgarParser
from api.edgar_tool import EdgarTool
from api.financial_data_aggregator import FinancialDataAggregator
from api.government_data import GovernmentData
from api.blockchain_integration import BlockchainIntegration
from api.crypto_exchange import CryptoExchange
from api.personal_finance import PersonalFinance
from api.business_finance import BusinessFinance
from api.analytics import FinancialAnalytics
from api.compliance import Compliance
from api.corporate_reports import CorporateReports
from api.budget_api import BudgetAPI
from api.omb_api import OMBAPI

app = Flask(__name__)

@app.route('/edgar/<cik>/<filing_type>', methods=['GET'])
def get_edgar_filings(cik, filing_type):
    parser = EdgarParser(cik)
    filings = parser.get_recent_filings(filing_type, count=5)
    return jsonify(filings)

@app.route('/government/<endpoint>', methods=['GET'])
def get_government_data(endpoint):
    gov_data = GovernmentData(endpoint)
    data = gov_data.get_data(params={})
    return jsonify(data)

@app.route('/crypto/<coin_id>', methods=['GET'])
def get_crypto_data(coin_id):
    exchange = CryptoExchange()
    market_data = exchange.get_market_data(coin_id)
    return jsonify(market_data)

@app.route('/personal_finance/summary', methods=['GET'])
def get_personal_finance_summary():
    finance = PersonalFinance()
    summary = finance.get_financial_summary()
    return jsonify(summary)

@app.route('/business_finance/summary', methods=['GET'])
def get_business_finance_summary():
    finance = BusinessFinance()
    summary = finance.get_financial_summary()
    return jsonify(summary)

@app.route('/compliance/<regulation>', methods=['GET'])
def check_compliance(regulation):
    compliance = Compliance()
    user_data = {"id_verification": True, "address_verification": True}
    is_compliant = compliance.check_compliance(regulation, user_data)
    return jsonify({"compliant": is_compliant})

if __name__ == "__main__":
    app.run(debug=True)
