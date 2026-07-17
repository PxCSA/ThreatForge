from fastapi import FastAPI

app = FastAPI(
    title="ThreatForge API",
    version="1.0.0",
    description="AI-powered Threat Intelligence Dashboard"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ThreatForge API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }