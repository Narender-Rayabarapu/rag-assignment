from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search_documents(query_embedding, documents, model):
    scores = []

    for doc in documents:
        doc_embedding = model.encode(doc["content"]).reshape(1, -1)

        similarity = cosine_similarity(
            query_embedding.reshape(1, -1),
            doc_embedding
        )[0][0]

        scores.append({
            "document": doc,
            "score": similarity
        })

    scores.sort(key=lambda x: x["score"], reverse=True)

    return scores[:3]