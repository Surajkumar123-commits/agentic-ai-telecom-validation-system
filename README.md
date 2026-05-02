# 🚀 Agentic AI Telecom Validation & Defect Intelligence System

## 🔷 Overview

This project is an AI-driven validation and defect intelligence system designed to automate telecom product validation across multiple enterprise platforms.

It compares:

* MPM Configuration Data
* Postman API Responses
* MPM Preview Tool Output

The system detects inconsistencies, identifies root causes, assigns ownership, and generates Jira-ready defect summaries automatically.

---

## 🧠 Architecture

MPM + Postman + Preview
↓
Platform Validation Agent
↓
Defect Analysis Agent
↓
Jira Comment Generator
↓
FastAPI APIs

---

## ⚙️ Key Features

* Cross-platform data validation (MPM, API, UI)
* Automated defect detection
* Root cause analysis (UI / Backend / Ops)
* Ownership recommendation
* Jira-ready comment generation
* End-to-end pipeline execution

---

## 🔌 API Endpoints

* POST `/platform-validation`
* POST `/defect-analysis`
* POST `/jira-comment`
* POST `/jira-comment-text`
* POST `/run-full-pipeline`
* GET `/health`

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Pandas
* REST APIs
* JSON

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn api.app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Sample Output

✔ Detects mismatches across platforms
✔ Assigns ownership (UI / Backend)
✔ Generates structured Jira comments

---
## 💼 Business Impact
- Reduces manual validation effort across telecom platforms
- Identifies defects before production deployment
- Speeds up defect triage and ownership assignment

## 🔮 Future Enhancements
- Integrate with real Jira APIs
- Add LLM-based root cause explanation
- Build UI dashboard for monitoring

## 📁 Project Structure
api/ → FastAPI application
src/agents/ → Validation, Defect, Jira agents
data/ → Sample input datasets
screenshots/ → README visuals


## ⚠️ Disclaimer

This project uses sample data and does not include any confidential enterprise information.
