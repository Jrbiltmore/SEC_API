
# /docs/API_Documentation.md
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010126

# NextGenFinancialSystem API Documentation

## Overview
This documentation provides an overview of the APIs available in the NextGenFinancialSystem. Each API is designed to facilitate different aspects of financial data management, analysis, and integration.

## API Endpoints

### EDGAR Parser
- **Endpoint**: `/api/edgar_parser.py`
- **Description**: Parses data from the EDGAR database.
- **Methods**:
  - `get_filing_urls(filing_type, count)`: Retrieves URLs for the specified type of filings.
  - `parse_filing(filing_url)`: Parses the filing at the given URL and extracts relevant data.
  - `get_recent_filings(filing_type, count)`: Retrieves and parses recent filings.

### EDGAR Tool
- **Endpoint**: `/api/edgar_tool.py`
- **Description**: Provides tools for interacting with the EDGAR database.
- **Methods**:
  - `fetch_filing_index(filing_type)`: Fetches the filing index for the specified type of filings.
  - `extract_filing_info(soup)`: Extracts filing information from the soup object.
  - `get_filing_data(filing_type)`: Retrieves and parses filing data.

### Financial Data Aggregator
- **Endpoint**: `/api/financial_data_aggregator.py`
- **Description**: Aggregates financial data from various sources.
- **Methods**:
  - `fetch_data(source)`: Fetches data from the specified source.
  - `aggregate_data()`: Aggregates data from all sources.
  - `get_aggregated_data()`: Returns aggregated data.

### Government Data
- **Endpoint**: `/api/government_data.py`
- **Description**: Handles government financial data.
- **Methods**:
  - `fetch_data(params)`: Fetches data from the government API.
  - `get_data(params)`: Retrieves government data.

### Blockchain Integration
- **Endpoint**: `/api/blockchain_integration.py`
- **Description**: Integrates blockchain data.
- **Methods**:
  - `get_block(block_number)`: Retrieves block data by block number.
  - `get_transaction(tx_hash)`: Retrieves transaction data by transaction hash.

### Crypto Exchange
- **Endpoint**: `/api/crypto_exchange.py`
- **Description**: Manages cryptocurrency exchange data.
- **Methods**:
  - `get_market_data(coin_id)`: Retrieves market data for the specified coin.
  - `get_exchange_rates()`: Retrieves current exchange rates.
  - `get_coin_info(coin_id)`: Retrieves information about the specified coin.

### Personal Finance
- **Endpoint**: `/api/personal_finance.py`
- **Description**: Manages personal finance data.
- **Methods**:
  - `add_income(source, amount)`: Adds an income entry.
  - `add_expense(category, amount)`: Adds an expense entry.
  - `get_balance()`: Retrieves the current balance.
  - `get_financial_summary()`: Retrieves a summary of financial data.

### Business Finance
- **Endpoint**: `/api/business_finance.py`
- **Description**: Manages business finance data.
- **Methods**:
  - `add_revenue(source, amount)`: Adds a revenue entry.
  - `add_expense(category, amount)`: Adds an expense entry.
  - `get_balance()`: Retrieves the current balance.
  - `get_financial_summary()`: Retrieves a summary of financial data.

### Analytics
- **Endpoint**: `/api/analytics.py`
- **Description**: Performs financial data analysis.
- **Methods**:
  - `calculate_moving_average(column, window)`: Calculates the moving average for the specified column.
  - `calculate_volatility(column, window)`: Calculates the volatility for the specified column.
  - `perform_regression(x_column, y_column)`: Performs a regression analysis.

### Compliance
- **Endpoint**: `/api/compliance.py`
- **Description**: Ensures compliance with financial regulations.
- **Methods**:
  - `add_regulation(name, details)`: Adds a new regulation.
  - `check_compliance(name, data)`: Checks if the provided data complies with the specified regulation.
  - `get_regulations()`: Retrieves all regulations.

### Corporate Reports
- **Endpoint**: `/api/corporate_reports.py`
- **Description**: Handles corporate financial reports.
- **Methods**:
  - `add_report(title, content)`: Adds a new report.
  - `get_report(title)`: Retrieves the report with the specified title.
  - `get_all_reports()`: Retrieves all reports.

### Budget API
- **Endpoint**: `/api/budget_api.py`
- **Description**: Manages budget data.
- **Methods**:
  - `create_budget(name, total_amount)`: Creates a new budget.
  - `add_expense(budget_name, category, amount)`: Adds an expense to the specified budget.
  - `get_budget_summary(budget_name)`: Retrieves a summary of the specified budget.

### OMB API
- **Endpoint**: `/api/omb_api.py`
- **Description**: Handles data from the Office of Management and Budget.
- **Methods**:
  - `fetch_data(params)`: Fetches data from the OMB API.
  - `get_data(params)`: Retrieves OMB data.

## Contact
For more information, please contact Jacob Thomas Messer Redmond.
