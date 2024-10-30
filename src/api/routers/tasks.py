from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

children = ["Tymek", "Józio", "Tosia", "Marysia"]
adults = ["Ania", "Tomek"]

message = {
    "INFO": "method not implemented"
}

@router.get(path="/tasks/", status_code=status.HTTP_200_OK, tahs=["tasks"])
def get_tasks(is_active: bool | None = True):
    #TODO implement
    return JSONResponse(status_code=status.HTTP_200_OK, content=message)
@router.put(path="/tasks/", status_code=status.HTTP_201_CREATED, tags=["tasks"])
def add_task():
    #TODO implement
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=message)
