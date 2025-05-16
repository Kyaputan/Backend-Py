from sqlalchemy import Column, Integer, String, Text
from database import Base

class UserDB(Base):
    __tablename__ = "python_DB"
    id = Column(Integer, primary_key=True, index=True ,autoincrement=True)
    name = Column(String(100), index=True)
    email = Column(Text, nullable=True)
    password = Column(String(255), nullable=False)