

import pandas as pd
from pathlib import Path

# Project folder path
BASE_PATH = Path(__file__).parent

DATA_FILE = BASE_PATH / "processed" / "validated_transactions.csv"


# Load dataset
def load_data():
    return pd.read_csv(DATA_FILE)


# 1. Positive transaction amount
def test_positive_transaction_amounts():
    df = load_data()
    assert (df["transaction_amount"] > 0).all()


# 2. Valid fraud flags
def test_fraud_flags_are_valid():
    df = load_data()
    assert df["is_fraud"].isin([0, 1]).all()


# 3. Valid transaction dates
def test_transaction_dates_are_valid():
    df = load_data()
    dates = pd.to_datetime(
        df["transaction_date"], errors="coerce"
    )
    assert dates.notna().all()


# 4. Valid account balance
def test_account_balance_is_valid():
    df = load_data()
    assert (df["account_balance"] >= 0).all()


# 5. Valid credit score
def test_credit_score_is_valid():
    df = load_data()
    assert df["credit_score"].between(300, 900).all()


# 6. Transaction IDs not missing
def test_transaction_ids_are_not_missing():
    df = load_data()
    assert df["transaction_id"].notna().all()


# 7. Transaction IDs unique
def test_transaction_ids_are_unique():
    df = load_data()
    assert df["transaction_id"].is_unique


# 8. Valid transaction status
def test_transaction_status_is_valid():
    df = load_data()
    valid_status = ["Success", "Failed", "Pending", "Reversed"]
    assert df["transaction_status"].isin(valid_status).all()


# 9. Valid transaction direction
def test_transaction_direction_is_valid():
    df = load_data()
    assert df["transaction_direction"].isin(
        ["Debit", "Credit"]
    ).all()


# 10. Valid transaction hour
def test_transaction_hour_is_valid():
    df = load_data()
    assert df["transaction_hour"].between(0, 23).all()
