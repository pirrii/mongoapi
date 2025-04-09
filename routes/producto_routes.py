from fastapi import APIRouter, HTTPException
from models.producto_models import Producto
from services.producto_service import obtener_productos, producto_por_id, crear_producto, eliminar_producto, actualizar_producto

router = APIRouter()

#Start api is available
@router.get("")
def start_productos():
    return {"message": "Welcome to productos services into de global API"}

# Get all products
@router.get("/productos", response_model=list)
async def obtener_productos_endpoint():
    productos = obtener_productos()
    return productos

# Get product by ID
@router.get("/productos/{producto_id}")
async def producto_endpoint(producto_id: str):
    producto = producto_por_id(producto_id)
    if producto:
        return producto
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.post("/productos")
async def crear_producto_endpoint(producto: Producto):
    producto_dict = producto.dict()  # Convierte el modelo en un diccionario
    producto_id = crear_producto(producto_dict)
    return {"id": producto_id}  # Devuelve el ID del producto insertado

@router.delete("/productos/{producto_id}")
async def eliminar_producto_endpoint(producto_id: str):
    if eliminar_producto(producto_id):
        return {"message": "Producto eliminado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
@router.put("/productos/{producto_id}")
async def actualizar_producto_endpoint(producto_id: str, producto: Producto):
    producto_dict = producto.dict()  # Convierte el modelo en un diccionario
    if actualizar_producto(producto_id, producto_dict):
        return {"message": "Producto actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
