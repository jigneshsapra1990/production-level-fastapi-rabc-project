from sqlalchemy import String, Column
from app.models.base import BaseModel

class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String, unique=True, nullable=False)