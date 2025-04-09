from fastapi import APIRouter, HTTPException
from services.recomendacion_service import (
    recomendar_por_categoria,
    recomendar_populares,
    recomendar_relacionados
)

router = APIRouter()

@router.get("/recomendaciones/categoria/{categoria}")
async def recomendaciones_por_categoria(categoria: str, limite: int = 5):
    productos = recomendar_por_categoria(categoria, limite)
    if productos:
        return productos
    else:
        raise HTTPException(status_code=404, detail="No se encontraron productos en esta categoría")

@router.get("/recomendaciones/populares")
async def recomendaciones_populares(limite: int = 5):
    productos = recomendar_populares(limite)
    return productos

@router.get("/recomendaciones/relacionados/{producto_id}")
async def recomendaciones_relacionadas(producto_id: str, limite: int = 5):
    productos = recomendar_relacionados(producto_id, limite)
    if productos:
        return productos
    else:
        raise HTTPException(status_code=404, detail="No se encontraron productos relacionados")