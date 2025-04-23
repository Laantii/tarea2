# archivo: models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vuelo(Base):
    __tablename__ = 'vuelos'

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=False)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    estado = Column(String, nullable=False)
