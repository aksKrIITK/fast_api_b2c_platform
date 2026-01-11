from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/")
async def list_orders():
    return {"message": "list orders - stub"}
