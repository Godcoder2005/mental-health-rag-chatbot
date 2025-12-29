from fastapi import FastAPI
from pydantic import BaseModel
from rag import retrieve_context
from llm_chain import generate_response

app = FastAPI(title="Mental Health Chatbot")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    context = retrieve_context(req.message)
    answer = generate_response(context, req.message)
    print(req.message)
    print(context)
    return ChatResponse(response=answer)
