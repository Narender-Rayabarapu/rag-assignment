import json

def load_documents():
    with open("backend/docs.json", "r") as f:
        return json.load(f)