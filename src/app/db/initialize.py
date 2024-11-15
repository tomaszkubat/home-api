from pydantic_sqlite import DataBase

from schemas import Status
def initialize_db():

    db = DataBase()

    statuses = [
        Status(id=1, name="DONE"),
        Status(id=2, name="PENDING")
    ]

    for s in statuses:
        db.add("Status", s)