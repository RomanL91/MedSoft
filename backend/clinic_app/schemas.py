from pydantic import BaseModel, ConfigDict


class ClinicBase(BaseModel):
    title: str
    description: str


class Clinic(ClinicBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ClinicCreate(ClinicBase):
    pass


class ClinicUpdate(ClinicBase):
    pass


class ClinicUpdatePartial(ClinicBase):
    title: str | None = None
    description: str | None = None
