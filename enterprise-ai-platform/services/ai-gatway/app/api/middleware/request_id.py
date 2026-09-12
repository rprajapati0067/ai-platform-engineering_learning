import logging
import time
import uuid

from fastapi import Request

from app.core.metrics import (
    http_request_duration_seconds,
    http_requests_total,
)
from app.core.request_context import request_id_context

logger = logging.getLogger(__name__)


async def request_id_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    token = request_id_context.set(request_id)

    start_time = time.perf_counter()

    excluded_paths = {
        "/metrics",
        "/docs",
        "/openapi.json",
    }

    try:
        response = await call_next(request)

        latency = time.perf_counter() - start_time
        latency_ms = latency * 1000

        if request.url.path not in excluded_paths:
            http_requests_total.labels(
                method=request.method,
                path=request.url.path,
                status_code=str(response.status_code),
            ).inc()

            http_request_duration_seconds.labels(
                method=request.method,
                path=request.url.path,
                status_code=str(response.status_code),
            ).observe(latency)

        logger.info(
            "HTTP request completed | method=%s | path=%s | "
            "status_code=%s | latency_ms=%.2f",
            request.method,
            request.url.path,
            response.status_code,
            latency_ms,
        )

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time-Ms"] = f"{latency_ms:.2f}"

        return response

    finally:
        request_id_context.reset(token)