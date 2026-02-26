

#  Financial Document Analyzer

### AI Internship – Debug Challenge Submission

> This project was completed as part of an **AI Internship Debug Challenge** focused on debugging, prompt optimization, and system design using CrewAI.

---

##  Project Overview

This repository contains a **financial document analysis system** built using **CrewAI**.
The original codebase had multiple **deterministic bugs**, **broken integrations**, and **inefficient LLM prompts**.

As part of this assignment, I:

* Identified and fixed all runtime and logical issues
* Optimized prompts for accuracy, structure, and cost efficiency
* Improved overall code reliability and repository hygiene

The system processes **financial PDF documents** and generates structured insights such as key metrics, risks, and summaries.

---

##  Bugs Identified & Fixes

###  `agents.py`

**Issues**

* Circular reference: `llm = llm`
* Incorrect import path for `Agent`
* Wrong parameter name (`tool` instead of `tools`)

**Fixes**

* Initialized a proper LLM instance
* Corrected Agent import
* Replaced `tool` with `tools` parameter

---

###  `tools.py`

**Issues**

* PDF parsing library not imported
* Missing `self` parameter in class methods
* Incomplete text extraction logic

**Fixes**

* Integrated `pdfplumber` for reliable PDF parsing
* Added missing `self` parameter
* Implemented full-page text extraction

---

###  `tasks.py`

**Issues**

* Incorrect agent references
* Task–agent mismatch

**Fixes**

* Corrected agent naming
* Ensured valid task-to-agent mapping

---

### `main.py`

**Issues**

* Runtime inputs (file path) not passed to the Crew
* Execution failed for dynamic document inputs

**Fixes**

* Passed inputs using `crew.kickoff(inputs={...})`
* Improved execution stability

---

##  Prompt Optimization

###  Original Problems

* Vague and underspecified prompts
* No role definition
* No enforced output format
* Higher hallucination risk

###  Improvements

* Added clear role definition (financial analyst)
* Step-by-step reasoning instructions
* Enforced structured JSON output

**Impact**

* More accurate responses
* Consistent, parseable outputs
* Reduced token waste

---

##  Setup & Usage

### Prerequisites

* Python 3.9+
* OpenAI API Key

### Installation

```bash
pip install -r requirements.txt
```

### Environment Variables

```bash
export OPENAI_API_KEY=your_api_key
```

### Run the Project

```bash
python main.py
```

---

## 📥 Input & 📤 Output

**Input**

* Path to a financial PDF document

**Output**

* Extracted financial metrics
* Risk indicators and anomalies
* Structured summary of insights

---

## Bonus Enhancements (Design-Level)

###  Queue Worker Model

* Designed async processing using **Redis + Celery**
* Enables concurrent document analysis
* Improves scalability and reliability

###  Database Integration

* Proposed persistent storage for:

  * Analysis results
  * Document metadata
  * Timestamps
* Supports auditing and result reuse

---

##  Tech Stack

* Python
* CrewAI
* LangChain
* OpenAI API
* pdfplumber
* Redis & Celery (Bonus)

---

## 📂Repository Hygiene

* Removed virtual environments and cache files
* Added `.gitignore` for clean version control
* Optimized repository size for deployment

---

##  Author

**Name:** *Arpit Gupta *
**Assignment:** AI Internship – Debug Challenge

---

## Summary

This submission demonstrates:

* Strong debugging and code analysis skills
* Effective LLM prompt engineering
* Production-aware system design thinking
* Clean documentation and repo practices

---

