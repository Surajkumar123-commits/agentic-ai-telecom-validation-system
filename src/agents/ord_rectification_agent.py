import pandas as pd

def run_ord_agent():
    df = pd.read_csv("data/sample_ord_data.csv")

    issues = []

    for _, row in df.iterrows():
        row_issues = []

        if row.get("price", 0) <= 0:
            row_issues.append("Invalid price")

        if not row.get("sku_id"):
            row_issues.append("Missing SKU ID")

        if row.get("validity", 0) <= 0:
            row_issues.append("Invalid validity")

        if row_issues:
            issues.append({
                "sku_id": row.get("sku_id"),
                "issues": row_issues
            })

    return {
        "agent": "ORD Rectification",
        "issue_count": len(issues),
        "results": issues
    }