from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    nombre: str
    descripcion: Optional[str]
    precio: float
    stock: int
    categoria: Optional[str]
    popularidad: Optional[int] = 0