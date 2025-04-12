from fastapi import FastAPI
from pydantic import BaseModel
from scripts.qa_model import get_answer

app = FastAPI()

class QARequest(BaseModel):
    context: str
    question: str

@app.post("/qa")
def answer(req: QARequest):
    answer = get_answer(req.context, req.question)
    return {"answer": answer}