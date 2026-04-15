import os
import google.generativeai as genai

class GeminiLLM:
    def __init__(self):
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def analyze_code(self, diff, rules):
        prompt = f"""
        You are a cybersecurity expert. Review the following code (Pull Request Diff) to detect potential security vulnerabilities.
        Base your review on the following OWASP rules:
        {rules}

        Code (Diff):
        {diff}

        Provide a structured report of vulnerabilities and proposed solutions. If there are no vulnerabilities, state that clearly.
        """
        response = self.model.generate_content(prompt)
        return response.text