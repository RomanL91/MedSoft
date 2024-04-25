from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core import Base

if TYPE_CHECKING:
    from clinic_app.models import Clinic


class Filial(Base):

    adress: Mapped[str | None] = mapped_column(String(250), unique=True)
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"))
    clinic: Mapped["Clinic"] = relationship(back_populates="filials")
