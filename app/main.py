from fastapi import FastAPI
from app.routes import basic
from app.metrics import metrics_router
from app.middleware import MetricsMiddleware  # ✅ Import here

app = FastAPI()

# Add metrics middleware
app.add_middleware(MetricsMiddleware)

# Register routers
app.include_router(basic.router)
app.include_router(metrics_router)
