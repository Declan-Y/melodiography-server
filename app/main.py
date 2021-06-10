from fastapi import FastAPI, Depends
from midi_generate import midi
from fastapi.responses import StreamingResponse
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import crud, models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/generate")
async def generate_melody():
    melody = midi.generate_random_melody()
    return StreamingResponse(melody, media_type="audio/midi", headers={"Content-Disposition": 'attachment; filename="test_file"'})


@app.post("/save")
async def save_drawing(drawing: schemas.CreateDrawing, db: Session = Depends(get_db)):
    return crud.create_drawing(drawing)

