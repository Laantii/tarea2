from pydantic import BaseModel, Field

class VueloBase(BaseModel):
    codigo: str = Field(..., example="AV123", description="Código del vuelo")
    origen: str = Field(..., example="Lima", description="Ciudad de origen")
    destino: str = Field(..., example="Buenos Aires", description="Ciudad destino")
    estado: str = Field(..., example="Programado", description="Estado del vuelo")

class VueloCreate(VueloBase):
    pass

class VueloResponse(VueloBase):
    id: int
    
    class Config:
        orm_mode = True  # ¡Esto es crítico!