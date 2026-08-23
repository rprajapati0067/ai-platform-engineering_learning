# pyrefly: ignore [missing-import]
import logging

from app.application.exceptions import LLMResponseError
from app.domain.llm import LLMProvider

# pyrefly: ignore [missing-import]
from app.domain.models import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    async def execute(self, request: ChatRequest) -> ChatResponse:
        logger.info("Processing chat request")

        response = await self.llm_provider.generate(request.message)
        if not response.strip():
            raise LLMResponseError("LLM returned an empty response")

        return ChatResponse(
            response=response,
            model=request.model,
        )
