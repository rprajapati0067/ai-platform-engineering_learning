# pyrefly: ignore [missing-import]
import logging

from opentelemetry import trace

from app.application.exceptions import LLMResponseError
from app.domain.llm import LLMProvider

# pyrefly: ignore [missing-import]
from app.domain.models import ChatRequest, ChatResponse

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    async def chat(self, request: ChatRequest) -> ChatResponse:
        with tracer.start_as_current_span("chat_service") as span:
            span.set_attribute("llm.model", request.model)

        response = await self.llm_provider.generate(
            request.message,
        )

        if not response.strip():
            raise LLMResponseError("LLM returned an empty response")

        return ChatResponse(
            response=response,
            model=request.model,
        )

    execute = chat
