from abc import ABC, abstractmethod

from core.db_manager import db_manager

from clinic_app.clinic_repository import ClinicRepository


class IUnitOfWork(ABC):

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = db_manager.get_scope_session()

    async def __aenter__(self):
        self.session = self.session_factory()

        self.clinic = ClinicRepository(self.session)
        # место для раздолья в транзакции

    async def __aexit__(self, *args):
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
