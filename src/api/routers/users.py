from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import random

router = APIRouter()

children = ["Tymek", "Józio", "Tosia", "Marysia"]
adults = ["Ania", "Tomek"]


@router.get(path="/users/volunteer/", status_code=status.HTTP_200_OK, tags=["users"])
def get_volunteer(add_adults: bool | None = False):
    if add_adults:
        candidates = children + adults
    else:
        candidates = children
    volunteer = random.choice(candidates)
    message = {
        "volunteer": volunteer
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=message)
