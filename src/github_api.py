import os
import requests
import json

class GitHubAPI:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN")
        self.repo = os.environ.get("GITHUB_REPOSITORY")
        
        with open(os.environ.get("GITHUB_EVENT_PATH"), 'r') as f:
            event_data = json.load(f)
            self.pr_number = event_data.get("pull_request", {}).get("number")
            
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3.diff"
        }

    def get_pr_diff(self):
        url = f"https://api.github.com/repos/{self.repo}/pulls/{self.pr_number}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def post_comment(self, comment_body):
        url = f"https://api.github.com/repos/{self.repo}/issues/{self.pr_number}/comments"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.post(url, headers=headers, json={"body": comment_body})
        response.raise_for_status()