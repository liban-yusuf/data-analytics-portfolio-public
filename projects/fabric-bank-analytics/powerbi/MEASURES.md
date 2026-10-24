# Power BI dashboard — implementation specification
**Not yet built or published in Power BI.** Create a semantic model from the Lakehouse Delta table `curated_transactions` and add these measures:

```dax
Transactions = COUNTROWS(curated_transactions)
Flagged = CALCULATE([Transactions], curated_transactions[review_flag] = 1)
Flag Rate = DIVIDE([Flagged], [Transactions])
Chargebacks = CALCULATE([Transactions], curated_transactions[chargeback] = 1)
True Positives = CALCULATE([Transactions], curated_transactions[review_flag] = 1, curated_transactions[chargeback] = 1)
Precision Proxy = DIVIDE([True Positives], [Flagged])
Recall Proxy = DIVIDE([True Positives], [Chargebacks])
```

Build pages: Overview (cards and transaction volume), Risk Analysis (risk-score histogram and merchant category bars), Review Quality (precision/recall proxy and alert volume). Add a prominent notice: **synthetic data; chargeback is not confirmed fraud**. Validate measures against SQL and Python before sharing.
