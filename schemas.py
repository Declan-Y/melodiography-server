from pydantic import BaseModel
from uuid import UUID

class CreateDrawing(BaseModel):
    title: str


class Drawing(BaseModel):
    id: UUID
    title: str
    class Config:
        orm_mode = True
