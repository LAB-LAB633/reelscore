from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ReelScore API",
    description="Sahteyi temizle, gerçeği gör.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "ReelScore API Çalışıyor! 🚀",
        "docs": "/docs",
        "status": "online"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}
