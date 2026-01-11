from app.api.auth.routes import router as auth_router
from fastapi import FastAPI

app = FastAPI(
    title="Project Nexus",
    version="0.1.0",
)
app.include_router(auth_router)


@app.get("/health")
def health_checkup():
    return {"status": "ok"}
