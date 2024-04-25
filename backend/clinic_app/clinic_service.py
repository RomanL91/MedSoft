from core.base_unit_of_work import IUnitOfWork
from clinic_app.models import Clinic
from clinic_app.schemas import Clinic, ClinicCreate, ClinicUpdate, ClinicUpdatePartial


class ClinicService:
    async def create_clinic(self, uow: IUnitOfWork, new_clinic: ClinicCreate) -> Clinic:
        clinic_dict = new_clinic.model_dump()
        async with uow:
            clinic = await uow.clinic.create_obj(clinic_dict)
            await uow.commit()
            return clinic

    async def get_clinics(self, uow: IUnitOfWork) -> list[Clinic]:
        async with uow:
            return await uow.clinic.get_all_objs()

    async def get_clinic_by_id(self, uow: IUnitOfWork, clinic_id: int) -> Clinic:
        async with uow:
            return await uow.clinic.get_obj(id=clinic_id)

    async def update_clinic(
        self,
        uow: IUnitOfWork,
        clinic_id: int,
        clinic_update: ClinicUpdate | ClinicUpdatePartial,
        partial: bool = False,
    ) -> Clinic:
        data = clinic_update.model_dump(exclude_unset=partial)
        async with uow:
            clinic = await uow.clinic.update_obj(obj_id=clinic_id, data=data)
            await uow.commit()
            return clinic

    async def delete_clinic(self, uow: IUnitOfWork, clinic_id: int) -> None:
        async with uow:
            await uow.clinic.delete_obj(obj_id=clinic_id)
            await uow.commit()
