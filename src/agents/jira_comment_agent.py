def generate_jira_comment(defect_output):
    lines = []
    items = []

    lines.append("### 🔍 Validation Summary")

    for item in defect_output["details"]:
        lines.append(
            f"- **SKU**: {item['sku_id']}\n"
            f"  - **Issue**: {item['issue']}\n"
            f"  - **Owner**: {item['owner']}\n"
            f"  - **Root Cause**: {item['root_cause']}\n"
            f"  - **Action**: {item['action']}"
        )

        items.append({
            "sku_id": item["sku_id"],
            "issue": item["issue"],
            "owner": item["owner"],
            "root_cause": item["root_cause"],
            "action": item["action"]
        })

    return {
        "agent": "Jira Comment Generator",
        "comment": "\n".join(lines),
        "items": items
    }