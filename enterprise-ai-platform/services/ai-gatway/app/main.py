import logging

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.api.middleware.request_id import request_id_middleware
from app.api.routes.chat import router as chat_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging(settings.log_level)

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)

app.middleware("http")(request_id_middleware)

logger.info("AI Gateway started")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/version")
async def version() -> dict[str, str]:
    return {
        "service": "ai-gateway",
        "version": "0.1.0",
    }


@app.get("/metrics")
async def metrics() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.include_router(chat_router)
