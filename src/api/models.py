from pydantic import BaseModel

class TaskBody(BaseModel):
    description: str
    priority: int | None = None
    is_complete: bool = False

class OperatorBody(BaseModel):
    name: str
