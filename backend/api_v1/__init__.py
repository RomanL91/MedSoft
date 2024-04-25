from fastapi import APIRouter

from .clinic_api.views import router as clinic_router
from .filial_api.views import router as filial_router


router = APIRouter()

router.include_router(router=clinic_router, prefix="/clinics")
router.include_router(router=filial_router, prefix="/filials")
