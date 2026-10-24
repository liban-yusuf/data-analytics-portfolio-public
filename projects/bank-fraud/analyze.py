"""Reproducible rule-based fraud triage on synthetic transactions (stdlib only)."""
import csv
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load_data(path=HERE / "transactions.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    con = sqlite3.connect(":memory:")
    con.execute("""CREATE TABLE transactions (
        transaction_id TEXT PRIMARY KEY, customer_id TEXT, amount REAL,
        merchant_category TEXT, country TEXT, hour INTEGER,
        is_international INTEGER, is_new_device INTEGER, chargeback INTEGER)""")
    for row in rows:
        con.execute("INSERT INTO transactions VALUES (?,?,?,?,?,?,?,?,?)",
                    (row["transaction_id"], row["customer_id"], float(row["amount"]),
                     row["merchant_category"], row["country"], int(row["hour"]),
                     int(row["is_international"]), int(row["is_new_device"]),
                     int(row["chargeback"])))
    return con

def scored_rows(con):
    return con.execute("""SELECT transaction_id, amount, chargeback,
       (CASE WHEN amount >= 1500 THEN 2 ELSE 0 END
        + CASE WHEN hour BETWEEN 0 AND 5 THEN 1 ELSE 0 END
        + CASE WHEN is_international = 1 THEN 1 ELSE 0 END
        + CASE WHEN is_new_device = 1 THEN 2 ELSE 0 END) AS risk_score
       FROM transactions ORDER BY transaction_id""").fetchall()

def metrics(rows, threshold=4):
    flagged = [r for r in rows if r[3] >= threshold]
    actual = [r for r in rows if r[2] == 1]
    true_positive = sum(r[2] == 1 for r in flagged)
    return {"transactions": len(rows), "chargebacks": len(actual),
            "flagged": len(flagged), "true_positive": true_positive,
            "precision": true_positive / len(flagged) if flagged else 0,
            "recall": true_positive / len(actual) if actual else 0}

if __name__ == "__main__":
    con = load_data()
    result = metrics(scored_rows(con))
    for key, value in result.items():
        print(f"{key}: {value:.2%}" if key in ("precision", "recall") else f"{key}: {value}")
    con.close()
