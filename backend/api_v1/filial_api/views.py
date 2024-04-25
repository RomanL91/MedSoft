from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from filial_app import crud, schemas

from api_v1.filial_api.dependencies import get_filial_by_id

from core.db_manager import db_manager


router = APIRouter(tags=["Filials"])


@router.get("/", response_model=list[schemas.Filial])
async def get_all_filials(
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
):
    return await crud.get_all_filials(session=session)


@router.post("/", response_model=schemas.Filial, status_code=status.HTTP_201_CREATED)
async def create_filial(
    new_filial: schemas.FilialCreate,
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
):
    return await crud.create_filial(session=session, new_filial=new_filial)


@router.get("/{filial_id}", response_model=schemas.Filial)
async def get_filial(filial: schemas.Filial = Depends(get_filial_by_id)):
    return filial


@router.put("/{filial_id}/", response_model=schemas.Filial)
async def update_filial(
    filial_update: schemas.FilialUpdate,
    filial: schemas.Filial = Depends(get_filial_by_id),
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
):
    return await crud.update_filial(
        session=session, filial=filial, filial_update=filial_update
    )


@router.patch("/{clinic_id}/")
async def update_filial(
    filial_update: schemas.FilialUpdate,
    filial: schemas.Filial = Depends(get_filial_by_id),
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
):
    return await crud.update_filial(
        session=session,
        filial=filial,
        filial_update=filial_update,
        partial=True,
    )


@router.delete("/{filial_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_filial(
    filial: schemas.Filial = Depends(get_filial_by_id),
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
) -> None:
    await crud.delete_filial(session=session, filial=filial)
