import logging

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.api.routes.paper_trade import router as paper_trade_router
from app.api.routes.stocks import router as stocks_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Stock Investment & Trading Platform Engine",
    version="1.0.0",
    description="Microservice providing 10-year fundamental analysis, valuation percentiles, multi-agent AI research, and risk-based position sizing for Indian equities.",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(stocks_router)
app.include_router(paper_trade_router)


@app.get("/health")
async def health() -> dict:
    return {"status": "healthy", "service": "stock-analysis-service"}


@app.get("/version")
async def version() -> dict:
    return {
        "service": "stock-analysis-service",
        "version": "0.1.0",
        "market": "NSE/BSE India",
    }


@app.get("/metrics")
async def metrics() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
