from sqlalchemy import Column, Integer, String
from config.dbp import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50))
    score = Column(Integer)