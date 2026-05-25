from sentence_transformers import SentenceTransformer
from backend.embeddings import generate_embedding
from backend.retrieval import search_documents
from backend.storage import load_documents
from backend.llm import ask_llm

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = load_documents()

def process_query(question):

    query_embedding = model.encode(question)

    results = search_documents(
        query_embedding,
        documents,
        model
    )

    best_score = results[0]["score"]

    if best_score < 0.3:
        return "I do not have enough information."

    context = "\n".join([
        r["document"]["content"]
        for r in results
    ])

    prompt = f"""
You are a helpful assistant.

Use only the provided context.

Context:
{context}

Question:
{question}
"""

    return ask_llm(prompt)