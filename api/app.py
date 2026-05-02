from fastapi import FastAPI
from src.agents.ord_rectification_agent import run_ord_agent
from src.agents.platform_validation_agent import run_platform_validation
from src.agents.defect_analysis_agent import run_defect_analysis
from src.agents.platform_validation_agent import run_platform_validation
from src.agents.jira_comment_agent import generate_jira_comment
from src.agents.defect_analysis_agent import run_defect_analysis
from src.agents.platform_validation_agent import run_platform_validation
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic AI System Running Successfully 🚀"}

@app.post("/ord-rectification")
def ord_rectification():
    return run_ord_agent()

@app.post("/platform-validation")
def platform_validation():
    return run_platform_validation()

@app.post("/defect-analysis")
def defect_analysis():
    validation_output = run_platform_validation()
    return run_defect_analysis(validation_output)

@app.post("/jira-comment")
def jira_comment():
    validation_output = run_platform_validation()
    defect_output = run_defect_analysis(validation_output)
    return generate_jira_comment(defect_output)

@app.post("/jira-comment-text", response_class=PlainTextResponse)
def jira_comment_text():
    validation_output = run_platform_validation()
    defect_output = run_defect_analysis(validation_output)
    result = generate_jira_comment(defect_output)
    return result["comment"]

@app.post("/run-full-pipeline")
def run_full_pipeline():
    v = run_platform_validation()
    d = run_defect_analysis(v)

    d["details"] = sorted(d.get("details", []), key=lambda x: x.get("sku_id", ""))

    j = generate_jira_comment(d)

    return {
        "summary": {
            "validation_issues": v["issue_count"],
            "defect_items": d["total_issues"],
        },
        "top_issues": d["details"],
        "jira_comment": j["comment"],
    }


# ✅ NO SPACES BEFORE THIS
@app.get("/health")
def health():
    return {"status": "ok"}