from clinic_app.models import Clinic
from core.base_repository import SQLAlchemyRepository


class ClinicRepository(SQLAlchemyRepository):
    model = Clinic
