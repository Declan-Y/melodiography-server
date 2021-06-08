from fastapi import FastAPI
from midi_generate import midi
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/generate")
async def generate_melody():
    melody = midi.generate_random_melody()
    return StreamingResponse(melody, media_type="audio/midi", headers={"Content-Disposition": 'attachment; filename="test_file"'})