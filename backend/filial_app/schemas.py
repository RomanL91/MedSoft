from pydantic import BaseModel, ConfigDict


class FilialBase(BaseModel):
    adress: str
    clinic_id: int


class Filial(FilialBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class FilialCreate(FilialBase):
    pass


class FilialUpdate(FilialBase):
    pass


class FilialUpdatePartical(FilialBase):
    adress: str | None = None
