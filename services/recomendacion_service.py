from db.database import database

def recomendar_por_categoria(categoria: str, limite: int = 5):
    productos_collection = database.get_collection("productos")
    productos = list(productos_collection.find({"categoria": categoria}).sort("popularidad", -1).limit(limite))
    for producto in productos:
        producto["_id"] = str(producto["_id"])  # Convierte ObjectId a string
    return productos

def recomendar_populares(limite: int = 5):
    productos_collection = database.get_collection("productos")
    productos = list(productos_collection.find().sort("popularidad", -1).limit(limite))
    for producto in productos:
        producto["_id"] = str(producto["_id"])  # Convierte ObjectId a string
    return productos

def recomendar_relacionados(producto_id: str, limite: int = 5):
    from bson import ObjectId  # Import necesario para manejar ObjectId
    productos_collection = database.get_collection("productos")
    producto = productos_collection.find_one({"_id": ObjectId(producto_id)})
    if not producto:
        return None
    categoria = producto.get("categoria")
    productos_relacionados = list(productos_collection.find({"categoria": categoria, "_id": {"$ne": ObjectId(producto_id)}}).limit(limite))
    for relacionado in productos_relacionados:
        relacionado["_id"] = str(relacionado["_id"])  # Convierte ObjectId a string
    return productos_relacionados