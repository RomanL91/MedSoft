from typing import Annotated

#
from fastapi import Path, Depends, HTTPException, status

#
from sqlalchemy.ext.asyncio import AsyncSession

#
from filial_app import crud
from filial_app.models import Filial

#
from core.db_manager import db_manager


async def get_filial_by_id(
    filial_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_manager.scope_session_dependency),
) -> Filial:
    filial = await crud.get_filial(session=session, filial_id=filial_id)
    if filial is not None:
        return filial
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Filial {filial_id} not found!"
    )
