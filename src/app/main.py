from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers import users

docs_url = "/api/docs"
redoc_url = "/api/redoc"

app = FastAPI(
    docs_url=docs_url,
    redoc_url=redoc_url,
    title="Home API",
    description="My home API",
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/", description="Root endpoint")
def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"For docs see '{docs_url}', for redocs see '{redoc_url}'"})
