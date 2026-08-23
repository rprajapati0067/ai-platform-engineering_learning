from fastapi import APIRouter

from app.application.chat_service import ChatService
from app.domain.models import ChatRequest, ChatResponse
from app.infrastructure.llm.mock_provider import MockLLMProvider

router = APIRouter()
llm_provider = MockLLMProvider()
chat_service = ChatService(llm_provider)


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await chat_service.execute(request)
