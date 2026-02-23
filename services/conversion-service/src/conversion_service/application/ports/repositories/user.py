from abc import ABC, abstractmethod

from conversion_service.domain.entitities.user_conversion_history import UserConversionHistory

class UserRepositoryInterface(ABC):
    @abstractmethod
    async def upload_user_conversion_history(self, user_id: str, user_history: UserConversionHistory) -> None:
        pass

    @abstractmethod
    async def get_user_conversion_history(self, user_id: str) -> UserConversionHistory:
        pass