import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.metrics import REQUEST_LATENCY

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        method = request.method
        endpoint = request.url.path
        status_code = str(response.status_code)

        REQUEST_LATENCY.labels(method=method, endpoint=endpoint, status_code=status_code).observe(duration)
        return response
