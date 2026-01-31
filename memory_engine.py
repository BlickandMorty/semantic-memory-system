import numpy as np
from datetime import datetime

class SemanticMemory:
    def __init__(self):
        self.storage = []

    def add_memory(self, text, importance, tags):
        memory = {
            "text": text,
            "importance": importance,
            "tags": tags,
            "timestamp": datetime.now(),
            "embedding": self._mock_embed(text) # In production, use SentenceTransformers
        }
        self.storage.append(memory)

    def _mock_embed(self, text):
        # Placeholder for actual vector embeddings
        return np.random.rand(128)

    def retrieve(self, query, top_k=3):
        # Logic for Similarity + Importance + Recency scoring
        # (This is the 'Score' seen in your Part 2 output)
        return sorted(self.storage, key=lambda x: x['importance'], reverse=True)[:top_k]