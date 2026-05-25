from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.rag import process_query

app = FastAPI()
conversation_store = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    sessionId: str
    message: str

@app.post("/api/chat")
def chat(request: ChatRequest):

    session_id = request.sessionId

    if session_id not in conversation_store:
        conversation_store[session_id] = []

    history = conversation_store[session_id]

    response = process_query(request.message)

    history.append({
        "user": request.message,
        "assistant": response
    })

    conversation_store[session_id] = history[-5:]

    return {
        "reply": response,
        "history": conversation_store[session_id]
    }