from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    model: str


class ChatResponse(BaseModel):
    response: str
    model: str
