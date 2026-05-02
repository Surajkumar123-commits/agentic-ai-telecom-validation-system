def run_defect_analysis(validation_output):

    analysis = []

    for item in validation_output["results"]:
        sku = item["sku_id"]
        issues = item["issues"]

        for issue in issues:
            if "Postman" in issue:
                team = "Backend/API Team"
                root_cause = "API response mismatch or deployment issue"
                action = "Check API logs and response payload"

            elif "Preview" in issue:
                team = "UI/Frontend Team"
                root_cause = "UI rendering or cache issue"
                action = "Check preview rendering and UI configs"

            else:
                team = "Configuration Team"
                root_cause = "Incorrect configuration in MPM"
                action = "Revalidate configuration entries"

            analysis.append({
                "sku_id": sku,
                "issue": issue,
                "owner": team,
                "root_cause": root_cause,
                "action": action
            })

    return {
        "agent": "Defect Analysis",
        "total_issues": len(analysis),
        "details": analysis
    }