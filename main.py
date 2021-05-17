from fastapi import FastAPI
from midi_generate import midi

app = FastAPI()

@app.get("/generate")
async def generate():
    return {"message": "Hello World"}