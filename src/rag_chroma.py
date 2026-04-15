import chromadb

class RAGSystem:
    def __init__(self, rules_path="data/owasp_rules.txt"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("security_rules")
        self._load_rules(rules_path)

    def _load_rules(self, path):
        with open(path, "r", encoding="utf-8") as f:
            rules = f.readlines()
        
        documents = [rule.strip() for rule in rules if rule.strip()]
        ids = [str(i) for i in range(len(documents))]
        
        self.collection.add(
            documents=documents,
            ids=ids
        )

    def get_relevant_rules(self, query, n_results=5):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return "\n".join(results["documents"][0])