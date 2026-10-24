"""Monthly KPI trends using SQLite window functions; synthetic data."""
import sqlite3
db=sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE sales(month TEXT PRIMARY KEY, revenue INTEGER);
INSERT INTO sales VALUES ('2026-01',10000),('2026-02',12000),('2026-03',9000),('2026-04',13500);
""")
QUERY="""WITH trends AS (
 SELECT month,revenue,LAG(revenue) OVER (ORDER BY month) AS prior_revenue,
 SUM(revenue) OVER (ORDER BY month ROWS UNBOUNDED PRECEDING) AS cumulative_revenue
 FROM sales
) SELECT month,revenue,prior_revenue,cumulative_revenue,
 ROUND(100.0*(revenue-prior_revenue)/NULLIF(prior_revenue,0),2) AS mom_pct
 FROM trends ORDER BY month"""
rows=db.execute(QUERY).fetchall()
assert len(rows)==4 and rows[0][2] is None
assert rows[1][4]==20.0 and rows[-1][3]==44500
for row in rows: print(row)
