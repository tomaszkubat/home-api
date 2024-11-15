from datetime import datetime
from pydantic import BaseModel


class Status(BaseModel):
    id: str
    name: str


class Task(BaseModel):
    id: str
    status: str
    date: datetime.date


class User(BaseModel):
    id: str
    name: str


class TaskUser(BaseModel):
    task_id: str
    user_id: str
