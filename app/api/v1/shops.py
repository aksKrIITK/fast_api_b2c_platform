from fastapi import APIRouter

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("/")
async def list_shops():
    return {"message": "list shops - stub"}
