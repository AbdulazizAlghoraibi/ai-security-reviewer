# 🛡️ AI Security Code Reviewer (Automated DevSecOps Pipeline)

An automated CI/CD security reviewer built with Python, GitHub Actions, and Generative AI. It performs real-time code analysis on Pull Requests using a RAG (Retrieval-Augmented Generation) architecture grounded in OWASP security standards.

## 🚀 Key Features
* **Automated PR Reviews**: Triggers instantly on new or synchronized Pull Requests.
* **Context-Aware Analysis (RAG)**: Utilizes ChromaDB to fetch relevant OWASP security rules dynamically based on the code diff.
* **LLM-Powered Detection**: Leverages Google's Gemini API to identify vulnerabilities (e.g., SQLi, XSS) and propose concrete code fixes directly as PR comments.
* **Serverless Architecture**: Runs entirely within GitHub Actions, requiring no dedicated hosting.

## 🛠️ Technology Stack
* **AI/LLM**: Google Gemini API
* **Vector Database**: ChromaDB (Local RAG)
* **CI/CD**: GitHub Actions
* **Language**: Python 3.10

## ⚙️ How It Works
1. A developer opens a Pull Request.
2. GitHub Actions triggers the workflow, extracting the code `diff`.
3. The system queries the local ChromaDB vector database to retrieve the most relevant OWASP guidelines.
4. The `diff` and the retrieved context are sent to the LLM.
5. The LLM acts as a cybersecurity expert, analyzing the code and posting a structured review directly to the PR timeline.