-- SQLite: import transactions.csv into a table named transactions, or run analyze.py.
-- Chargeback is an outcome label used for evaluation, never for risk scoring.
WITH scored AS (
 SELECT *,
  (CASE WHEN amount >= 1500 THEN 2 ELSE 0 END
   + CASE WHEN hour BETWEEN 0 AND 5 THEN 1 ELSE 0 END
   + CASE WHEN is_international = 1 THEN 1 ELSE 0 END
   + CASE WHEN is_new_device = 1 THEN 2 ELSE 0 END) AS risk_score
 FROM transactions
)
SELECT CASE WHEN risk_score >= 4 THEN 'review' ELSE 'not_flagged' END AS decision,
 COUNT(*) AS transactions,
 SUM(chargeback) AS observed_chargebacks,
 ROUND(AVG(amount), 2) AS average_amount
FROM scored GROUP BY decision ORDER BY decision;
