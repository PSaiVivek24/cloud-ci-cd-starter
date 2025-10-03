from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

@app.get("/healthz")
def healthz(): return {"status": "ok"}

@app.get("/movies")
def movies():
    return [
        {"id": 1, "title": "Inception", "year": 2010, "rating": 8.8},
        {"id": 2, "title": "Interstellar", "year": 2014, "rating": 8.6},
        {"id": 3, "title": "The Dark Knight", "year": 2008, "rating": 9.0},
    ]
