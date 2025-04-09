from fastapi import FastAPI, Request
from routes.producto_routes import router as producto_router
from routes.recomendacion_routes import router as recomendacion_router


app = FastAPI(title="apimongo")

app.include_router(producto_router, prefix="/api")
app.include_router(recomendacion_router , prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI! crud mongoDB"} 






