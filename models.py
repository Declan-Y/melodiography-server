from database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Drawing(Base):
    __tablename__ = "drawings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)