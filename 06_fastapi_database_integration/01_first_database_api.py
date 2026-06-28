from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Database API is running"}
