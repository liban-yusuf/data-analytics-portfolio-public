# Fraud Alert Threshold Evaluation

**Status:** executable local learning exercise, synthetic data only.

## Business question
Compare review volume, precision and recall across five risk thresholds; chargeback is a proxy label.

## Run
From the repository root:
```bash
python3 projects/fraud-threshold-evaluation/analyze.py
```

## Skills demonstrated
Risk scoring, threshold sensitivity, confusion-matrix metrics, review workload and label limitations.

## Limitations
Chargebacks are not confirmed fraud. The tiny hand-crafted sample cannot estimate operational detection performance.

## Interview prompt
Explain the business trade-off, how you validated the numbers, and what you would improve with real-world data.
