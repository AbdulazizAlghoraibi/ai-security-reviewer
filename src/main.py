from github_api import GitHubAPI
from rag_chroma import RAGSystem
from gemini_llm import GeminiLLM

def main():
    github = GitHubAPI()
    rag = RAGSystem()
    llm = GeminiLLM()

    diff = github.get_pr_diff()
    
    if not diff or len(diff.strip()) == 0:
        return

    relevant_rules = rag.get_relevant_rules(diff)
    review_comment = llm.analyze_code(diff, relevant_rules)
    
    github.post_comment(review_comment)

if __name__ == "__main__":
    main()