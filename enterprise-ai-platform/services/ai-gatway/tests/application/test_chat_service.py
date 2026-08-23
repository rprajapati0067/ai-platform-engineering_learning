import pytest

from app.application.chat_service import ChatService
from app.application.exceptions import LLMResponseError
from app.domain.models import ChatRequest
from app.infrastructure.llm.another_fake_provider import AnotherFakeLLMProvider
from app.infrastructure.llm.empty_provider import EmptyLLMProvider
from app.infrastructure.llm.fake_provider import FakeLLMProvider


@pytest.mark.asyncio
async def test_chat_service_returns_llm_response():
    # Arrange
    provider = FakeLLMProvider()
    service = ChatService(provider)

    request = ChatRequest(message="Hello", model="fake-model")

    # Act
    response = await service.execute(request)
    # Assert
    assert response.response == "Fake AI response: Hello"
    assert response.model == "fake-model"


@pytest.mark.asyncio
async def test_chat_service_returns_another_llm_response():
    #  Arrange
    provider = AnotherFakeLLMProvider()
    service = ChatService(provider)

    request = ChatRequest(
        message="Hello",
        model="fake-model",
    )

    # Act
    response = await service.execute(request)
    # Assert
    assert response.response == "Another response"
    assert response.model == "fake-model"


@pytest.mark.asyncio
async def test_chat_service_raises_error_for_empty_llm_response():
    #  Arrange
    provider = EmptyLLMProvider()
    service = ChatService(provider)

    request = ChatRequest(
        message="Hello",
        model="fake-model",
    )

    # Act
    with pytest.raises(LLMResponseError):
        await service.execute(request)
