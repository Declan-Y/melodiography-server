from sqlalchemy.orm import Session

import models, schemas

def create_drawing(db: Session, drawing: schemas.CreateDrawing):
    db_drawing = models.Drawing(title=drawing.title)
    db.add(db_drawing)
    db.commit()
    db.refresh(db_drawing)
    return db_drawing
