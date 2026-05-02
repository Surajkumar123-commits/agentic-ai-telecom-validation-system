import pandas as pd
import json

def norm(x):
    if pd.isna(x):
        return ""
    return str(x).strip().lower()
def safe_float(x):
    try:
        return float(x)
    except:
        return 0.0

def run_platform_validation():

    mpm = pd.read_csv("data/sample_mpm_config.csv")
    postman = pd.read_csv("data/sample_postman_output.csv")

    with open("data/sample_preview_output.json", "r") as file:
        preview_data = json.load(file)

    preview = pd.DataFrame(preview_data)

    # Fix datatype
    mpm["sku_id"] = mpm["sku_id"].astype(str)
    postman["sku_id"] = postman["sku_id"].astype(str)
    preview["sku_id"] = preview["sku_id"].astype(str)

    # Merge
    merged = (
    mpm
    .merge(postman, on="sku_id", suffixes=("_mpm", "_postman"))
    .merge(preview, on="sku_id", suffixes=("", "_preview"))
)
    

    # ✅ LOOP MUST BE HERE
    issues = []

    for _, row in merged.iterrows():
        row_issues = []

        if norm(row["display_badge_mpm"]) != norm(row["display_badge_postman"]):
            row_issues.append("Badge mismatch MPM vs Postman")

        if norm(row["display_badge_mpm"]) != norm(row["display_badge"]):
            row_issues.append("Badge mismatch MPM vs Preview")

        if norm(row["upgrade_enabled_mpm"]) != norm(row["upgrade_enabled_postman"]):
            row_issues.append("Upgrade mismatch MPM vs Postman")

        if norm(row["upgrade_enabled_mpm"]) != norm(row["visible_on_upgrade"]):
            row_issues.append("Upgrade mismatch MPM vs Preview")

        if norm(row["device_channel_mpm"]) != norm(row["device_channel_postman"]):
            row_issues.append("Device channel mismatch MPM vs Postman")

        if float(row["price_mpm"]) != float(row["price_postman"]):
            row_issues.append("Price mismatch MPM vs Postman")

        if float(row["activation_fee_mpm"]) != float(row["activation_fee_postman"]):
            row_issues.append("Activation fee mismatch MPM vs Postman")

        if norm(row["discount_applied_mpm"]) != norm(row["discount_applied_postman"]):
            row_issues.append("Discount applied mismatch MPM vs Postman")

        if float(row["discount_value_mpm"]) != float(row["discount_value_postman"]):
            row_issues.append("Discount value mismatch MPM vs Postman")

        if norm(row["sort_order"]) != norm(row["sort_order_preview"]):
            row_issues.append("Sort order mismatch MPM vs Preview")

        if norm(row["new_addon"]) == "yes" and norm(row["addon_name"]) != norm(row["addon_name_preview"]):
            row_issues.append("Addon mismatch MPM vs Preview")

        if norm(row["changeset_status"]) != "staging live":
            row_issues.append("Changeset not live")

        if row_issues:
            issues.append({
                "sku_id": row["sku_id"],
                "issues": row_issues
            })
    return {
    "agent": "Platform Validation",
    "issue_count": len(issues),
    "results": issues
}        