"""Evaluate alert thresholds on the portfolio's synthetic fraud data."""
import csv
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1]/"bank-fraud"/"transactions.csv"
def risk(row):
    return (2*(float(row["amount"])>=1500)
            +(0<=int(row["hour"])<=5)
            +int(row["is_international"])
            +2*int(row["is_new_device"]))
def evaluate(rows,threshold):
    tp=fp=fn=0
    for row in rows:
        flagged=risk(row)>=threshold
        observed=int(row["chargeback"])==1
        tp+=int(flagged and observed)
        fp+=int(flagged and not observed)
        fn+=int(not flagged and observed)
    return {"threshold":threshold,"alerts":tp+fp,
            "precision":round(tp/(tp+fp),3) if tp+fp else None,
            "recall":round(tp/(tp+fn),3) if tp+fn else None}
if __name__=="__main__":
    with SOURCE.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    assert len(rows)==20
    for threshold in (2,3,4,5,6): print(evaluate(rows,threshold))
