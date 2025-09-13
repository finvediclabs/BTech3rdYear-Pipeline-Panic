from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    # Simulate environment mismatch bug
    env = os.getenv("APP_ENV", "dev")
    if env == "ci":
        return {"message": "Hello from CI!"}
    return {"message": "Hello from Dev!"}
