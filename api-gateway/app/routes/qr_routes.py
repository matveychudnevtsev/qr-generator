from fastapi import APIRouter

router = APIRouter()

@router.get("/generate")
async def generate_qr(data: str):
    # Placeholder for actual QR generation via qr-generator service
    return {"qr": f"generated-from-{data}"}
