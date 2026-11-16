# financial-data-processing-automation
Python-based financial data processing, validation, analysis, Excel report automation, and automated testing using Pandas, OpenPyXL, and Pytest.
# Financial Data Processing & Reporting Automation

## Project Overview
This project focuses on automating financial transaction data processing, validation, analysis, and Excel report generation using Python.

The project uses an Indian Banking Transactions dataset containing **550,000 records and 20 columns**.

The objective is to reduce manual data processing, identify data quality issues, generate financial insights, and automate reporting.

## Objectives
- Automate financial transaction data processing.
- Perform data quality checks and validation.
- Identify missing and invalid records.
- Analyze banking transaction patterns.
- Generate automated Excel reports.
- Maintain execution logs.
- Perform automated testing using Pytest.

## Technologies Used
- Python
- Pandas
- NumPy
- OpenPyXL
- Jupyter Notebook
- Pytest
- Logging

## Project Workflow

### 1. Data Loading
- Loaded 550,000 transaction records using Pandas.
- Verified dataset structure and required columns.

### 2. Data Validation & Cleaning
- Checked transaction amounts and dates.
- Validated account balances, credit scores, fraud flags, and transaction hours.
- Identified 19,422 records with missing loan type information.
- Separated exception records from validated transaction data.

### 3. Financial Data Analysis
Performed analysis on:
- Transaction status
- Debit and credit transactions
- Payment channels
- Monthly transaction trends
- Successful transactions
- Fraud by channel and merchant category

### 4. Excel Report Automation
- Generated an Excel report using OpenPyXL.
- Created 9 worksheets.
- Applied formatting and charts.

### 5. Logging
- Implemented Python logging to track automation execution.
- Generated an automation log file.

### 6. Automated Testing
Created 10 automated test cases using Pytest to validate:
- Positive transaction amounts
- Valid fraud flags
- Valid transaction dates
- Non-negative account balances
- Valid credit scores
- Non-missing transaction IDs
- Unique transaction IDs
- Valid transaction statuses
- Valid transaction directions
- Valid transaction hours

**Test Results: 10 Passed**

## Project Structure

```text
financial-data-processing-automation/
│
├── README.md
├── finance_automation.ipynb
├── financial_data_analysis.ipynb
├── test_finance_automation.py
│
├── processed/
│   ├── validated_transactions.csv
│   └── data_quality_exceptions.csv
│
└── reports/
    ├── Financial_Analysis_Report.xlsx
    └── automation.log
```

## How to Run

### Install Required Libraries

```bash
pip install pandas numpy openpyxl pytest
```

### Run the Automation
Open `finance_automation.ipynb` in Jupyter Notebook and execute the cells.

### Run Automated Tests

```bash
python -m pytest -v test_finance_automation.py
```

## Test Execution Result

```text
10 passed in 14.08s
```

All 10 automated test cases passed successfully.

## Key Outcomes
- Processed 550,000 financial transaction records.
- Identified and separated data quality exceptions.
- Automated financial data analysis.
- Generated a formatted Excel report with 9 worksheets.
- Implemented execution logging.
- Successfully executed 10 Pytest test cases.

## Author
Ritika Nampalliwar
