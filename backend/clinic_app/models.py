from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core import Base

if TYPE_CHECKING:
    from filial_app.models import Filial


class Clinic(Base):

    title: Mapped[str]
    description: Mapped[str]
    filials: Mapped[list["Filial"]] = relationship(back_populates="clinic")
