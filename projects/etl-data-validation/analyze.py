"""Validate a synthetic feed before reporting; Python standard library."""
from collections import Counter
from decimal import Decimal, InvalidOperation

ROWS=[
 {"id":"A1","amount":"100.00","status":"paid"},
 {"id":"A2","amount":"50.25","status":"paid"},
 {"id":"A2","amount":"50.25","status":"paid"},
 {"id":"A3","amount":"-5","status":"paid"},
 {"id":"A4","amount":"abc","status":"paid"},
 {"id":"A5","amount":"75.00","status":"cancelled"}
]
def validate(rows):
    seen=set(); accepted=[]; rejected=[]
    for row in rows:
        issues=[]
        if not row["id"] or row["id"] in seen: issues.append("duplicate_or_missing_id")
        seen.add(row["id"])
        try:
            amount=Decimal(row["amount"])
            if not amount.is_finite() or amount<0: issues.append("invalid_amount")
        except (InvalidOperation,ValueError):
            amount=None; issues.append("invalid_amount")
        if row["status"] not in ("paid","cancelled"): issues.append("invalid_status")
        if issues: rejected.append((row["id"],issues))
        else: accepted.append((row,amount))
    return accepted,rejected
if __name__=="__main__":
    accepted,rejected=validate(ROWS)
    paid=sum((amount for row,amount in accepted if row["status"]=="paid"),Decimal("0"))
    assert len(accepted)==3 and len(rejected)==3 and paid==Decimal("150.25")
    print("Accepted:",len(accepted),"Rejected:",rejected,"Paid total:",paid)
