from fastapi import FastAPI, Depends
from midi_generate import midi
from fastapi.responses import StreamingResponse
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud, schemas
from datetime import timedelta

from minio import Minio

app = FastAPI()

client = Minio('localhost:9001',secure=False, access_key="admin", secret_key="password" )
client.make_bucket("uploads")

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
    return crud.create_drawing(db, drawing)


@app.get("/put-presigned-url")
async def put_presigned_url():
    url = client.presigned_put_object("uploads", "object", expires=timedelta(hours=2))
    return url


@app.get("/get-presigned-url")
async def get_presigned_url():
    url = client.presigned_get_object("uploads", "object", expires=timedelta(hours=2))
    return url

