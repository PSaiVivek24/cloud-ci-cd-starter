from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/movies")
def movies():
    return [{"id": 1, "title": "Inception", "year": 2010}]
