# archivo: main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import crud
from typing import List

from fastapi.middleware.cors import CORSMiddleware

# Crear las tablas en la BD
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Gestión de Vuelos")

# Permitir CORS si se conecta desde HTML u otro cliente externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vuelos/", response_model=schemas.VueloResponse, summary="Crear un nuevo vuelo")
def crear_vuelo(vuelo: schemas.VueloCreate, db: Session = Depends(get_db)):
 
    return crud.crear_vuelo(db, vuelo)

@app.get("/vuelos/", response_model=List[schemas.VueloResponse])
def listar_vuelos(db: Session = Depends(get_db)):
    return crud.obtener_vuelos(db)

@app.get("/vuelos/{vuelo_id}", response_model=schemas.VueloResponse)
def obtener_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    vuelo = crud.obtener_vuelo(db, vuelo_id)
    if not vuelo:
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")
    return vuelo

@app.delete("/vuelos/{vuelo_id}", response_model=schemas.VueloResponse)
def borrar_vuelo(vuelo_id: int, db: Session = Depends(get_db)):
    vuelo = crud.eliminar_vuelo(db, vuelo_id)
    if not vuelo:
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")
    return vuelo
