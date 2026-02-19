from fastapi import APIRouter

from conversion_service.routes.conversion import router as conversion_router

router = APIRouter(prefix="/api/v1")

router.include_router(conversion_router)