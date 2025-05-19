from fastapi import FastAPI
from .routes import qr_routes, health

app = FastAPI()

app.include_router(qr_routes.router, prefix="/qr")
app.include_router(health.router, prefix="/health")


@app.get("/")
async def root():
    return {"message": "API Gateway"}
