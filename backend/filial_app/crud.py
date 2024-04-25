# sqlalchemy imports
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

# filial_app imports
from filial_app.models import Filial
from filial_app.schemas import FilialCreate, FilialUpdate, FilialUpdatePartical

# api_v1 imports
# from api_v1.clinic_api.dependencies import get_clinics_by_id


async def get_all_filials(session: AsyncSession) -> list[Filial]:
    stmt = select(Filial).order_by(Filial.id)
    result: Result = await session.execute(stmt)
    filials = result.scalars().all()
    return filials


# async def create_filial(session: AsyncSession, new_filial: FilialCreate) -> Filial:
#     new_filial = Filial(**new_filial.model_dump())
#     await get_clinics_by_id(new_filial.clinic_id, session=session)
#     session.add(new_filial)
#     await session.commit()
#     return new_filial


async def get_filial(session: AsyncSession, filial_id: int) -> Filial | None:
    return await session.get(Filial, filial_id)


async def update_filial(
    session: AsyncSession,
    filial: Filial,
    filial_update: FilialUpdate | FilialUpdatePartical,
    partial: bool = False,
) -> Filial:
    for k, v in filial_update.model_dump(exclude_unset=partial).items():
        setattr(filial, k, v)
    await session.commit()
    return filial


async def delete_filial(
    session: AsyncSession,
    filial: Filial,
) -> None:
    await session.delete(filial)
    await session.commit()
