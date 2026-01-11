from fastapi import APIRouter

router = APIRouter()

# include sub-routers
from . import auth, users, shops, products, orders  # noqa: F401

try:
    router.include_router(auth.router)
    router.include_router(users.router)
    router.include_router(shops.router)
    router.include_router(products.router)
    router.include_router(orders.router)
except Exception:
    pass
