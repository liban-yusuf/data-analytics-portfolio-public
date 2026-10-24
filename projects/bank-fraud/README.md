# Bank Fraud Detection — Rule-Based Transaction Triage

**Status:** reproducible learning case, not a production fraud detection system.  
**Tools:** Python standard library, SQLite, SQL, unittest.  
**Data:** 20 entirely synthetic transactions; no customer or bank records.

## Business question
Which transactions should an analyst review first, and how many observed chargebacks would a simple transparent risk rule capture?

## Method
Each transaction receives a score using only information available at transaction time:
- Amount >= 1,500 fictional currency units: +2
- Transaction between midnight and 05:59: +1
- International transaction: +1
- New device: +2

Score >= 4 triggers **manual review**, not an automatic fraud accusation. The `chargeback` field is used only as a retrospective proxy label for evaluation, **not** as a scoring input. Chargebacks are not synonymous with confirmed fraud.

## Run locally
From this folder:
```bash
python analyze.py
python -m unittest discover -s . -p 'test_*.py' -v
```
No external dependencies. Review `fraud_analysis.sql` for an equivalent SQL grouping of flagged and non-flagged transactions.

## Interpretation
The script reports flagged transactions, observed chargebacks, precision and recall on this small synthetic example. These numbers are illustrative only: the sample is hand-constructed, unrepresentative, and far too small to estimate real-world performance. False positives create review cost; false negatives create exposure. A real evaluation would require time-based holdout data, label-quality review, privacy safeguards, drift monitoring, and an operational review capacity constraint.

## What to discuss in an interview
1. Why separate a **risk indicator** from proof of fraud?
2. How does changing the score threshold affect precision and recall?
3. Why must chargeback labels not be used as an input feature?
4. What would you change with realistic transaction histories?

## Next iteration
Compare thresholds, segment by merchant category, visualize review workload in Power BI, and document model governance. **Microsoft Fabric deployment is a separate planned project, not completed here.**
