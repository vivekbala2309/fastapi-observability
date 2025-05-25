from fastapi import FastAPI
from app.routes import basic
from app import metrics

app = FastAPI()

# Include routers
app.include_router(basic.router)
app.include_router(metrics.metrics_router)
