from fastapi import APIRouter
from app.metrics import REQUEST_COUNT

router = APIRouter()

@router.get("/")
def read_root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return {"message": "GET received at root"}

@router.post("/submit")
def submit_data():
    REQUEST_COUNT.labels(method="POST", endpoint="/submit").inc()
    return {"message": "POST received at /submit"}

@router.put("/update")
def update_data():
    REQUEST_COUNT.labels(method="PUT", endpoint="/update").inc()
    return {"message": "PUT received at /update"}
