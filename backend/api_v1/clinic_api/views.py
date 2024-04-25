from fastapi import APIRouter, status

from clinic_app import schemas
from clinic_app.clinic_service import ClinicService

from api_v1.clinic_api.dependencies import UOF_Depends


router = APIRouter(tags=["Clinics"])


@router.post("/", response_model=schemas.Clinic, status_code=status.HTTP_201_CREATED)
async def create_clinic(new_clinic: schemas.ClinicCreate, uow: UOF_Depends):
    return await ClinicService().create_clinic(uow=uow, new_clinic=new_clinic)


@router.get("/", response_model=list[schemas.Clinic])
async def get_clinics(uow: UOF_Depends):
    return await ClinicService().get_clinics(uow)


@router.get("/{clinic_id}/", response_model=schemas.Clinic)
async def get_clinic_by_id(clinic_id: int, uow: UOF_Depends):
    return await ClinicService().get_clinic_by_id(uow=uow, clinic_id=clinic_id)


@router.put("/{clinic_id}/", response_model=schemas.Clinic)
async def update_clinic(
    uow: UOF_Depends,
    clinic_id: int,
    clinic_update: schemas.ClinicUpdate,
):
    return await ClinicService().update_clinic(
        uow=uow, clinic_id=clinic_id, clinic_update=clinic_update
    )


@router.patch("/{clinic_id}/", response_model=schemas.Clinic)
async def update_clinic(
    uow: UOF_Depends,
    clinic_id: int,
    clinic_update: schemas.ClinicUpdatePartial,
):
    return await ClinicService().update_clinic(
        uow=uow, clinic_id=clinic_id, clinic_update=clinic_update, partial=True
    )


@router.delete("/{clinic_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_clinic(uow: UOF_Depends, clinic_id: int) -> None:
    await ClinicService().delete_clinic(uow=uow, clinic_id=clinic_id)
