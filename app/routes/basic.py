from fastapi import APIRouter, Response, status
from app.metrics import REQUEST_COUNT

router = APIRouter()

@router.get("/")
def read_root():
    status_code = status.HTTP_200_OK
    REQUEST_COUNT.labels(method="GET", endpoint="/", status_code=str(status_code)).inc()
    return {"message": "GET received at root"}

@router.post("/submit")
def submit_data(success: bool = True):
    if success:
        status_code = status.HTTP_200_OK
        REQUEST_COUNT.labels(method="POST", endpoint="/submit", status_code=str(status_code)).inc()
        return {"message": "POST received at /submit"}
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        REQUEST_COUNT.labels(method="POST", endpoint="/submit", status_code=str(status_code)).inc()
        return {"error": "Bad request"}, status_code

@router.put("/update")
def update_data():
    status_code = status.HTTP_200_OK
    REQUEST_COUNT.labels(method="PUT", endpoint="/update", status_code=str(status_code)).inc()
    return {"message": "PUT received at /update"}
