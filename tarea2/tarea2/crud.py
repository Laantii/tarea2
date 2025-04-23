# archivo: crud.py

from sqlalchemy.orm import Session
import models
import schemas

def crear_vuelo(db: Session, vuelo: schemas.VueloCreate):
    db_vuelo = models.Vuelo(**vuelo.dict())
    db.add(db_vuelo)
    db.commit()
    db.refresh(db_vuelo)
    return db_vuelo

def obtener_vuelos(db: Session):
    return db.query(models.Vuelo).all()  # Retorna una lista de objetos Vuelo

def obtener_vuelo(db: Session, vuelo_id: int):
    return db.query(models.Vuelo).filter(models.Vuelo.id == vuelo_id).first()

def eliminar_vuelo(db: Session, vuelo_id: int):
    vuelo = obtener_vuelo(db, vuelo_id)
    if vuelo:
        db.delete(vuelo)
        db.commit()
    return vuelo
