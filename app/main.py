from fastapi import FastAPI

app = FastAPI(
    title="Project Nexus",
    version="0.1.0",
)


@app.get("/health")
def health_checkup():
    return {"status": "ok"}
