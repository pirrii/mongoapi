from bson import ObjectId
from db.database import database

#Obtener todos los productos
def obtener_productos():
    collection = database.get_collection("productos")  # Selecciona la colección "productos"
    productos = list(collection.find({}, {"_id": 0}))  # Excluye "_id"
    return productos

def producto_por_id(producto_id: str):
    productos_collection = database.get_collection("productos")
    producto = productos_collection.find_one({"_id": ObjectId(producto_id)})
    if producto:
        producto["_id"] = str(producto["_id"])  # Convierte ObjectId a string
    return producto

def crear_producto(producto: dict):
    productos_collection = database.get_collection("productos")
    resultado = productos_collection.insert_one(producto)
    return str(resultado.inserted_id)  # Devuelve el ID del producto insertado

def eliminar_producto(producto_id: str):
    productos_collection = database.get_collection("productos")
    resultado = productos_collection.delete_one({"_id": ObjectId(producto_id)})
    return resultado.deleted_count > 0  # Devuelve True si se eliminó un documento

def actualizar_producto(producto_id: str, producto_actualizado: dict):
    productos_collection = database.get_collection("productos")
    resultado = productos_collection.update_one(
        {"_id": ObjectId(producto_id)},
        {"$set": producto_actualizado}
    )
    return resultado.modified_count > 0  # Devuelve True si se actualizó un documento