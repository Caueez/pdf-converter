

from infra.database.implementation.repository import DatabaseRepository

from conversion_service.domain.entitities.user_conversion_history import UserConversionHistory

from conversion_service.domain.mappers.user_conversion_history import MapperUserConversionHistory

from conversion_service.application.ports.repositories.user import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, repo : DatabaseRepository) -> None:
        self._repo = repo
    
    async def upload_user_conversion_history(self, user_id: str, user_history: UserConversionHistory):
        if not user_id:
            raise ValueError("user_id is required")
        
        await self._repo.execute(
            """
                UPDATE user_conversion_history
                SET plan_name = $1, active_jobs = $2, monthly_jobs = $3
                WHERE user_id = $4;
            """   , 
            user_history.plan.name, user_history.active_jobs, user_history.monthly_jobs, user_id
        )
        
    async def get_user_conversion_history(self, user_id: str):
        if not user_id:
            raise ValueError("user_id is required")
        
        history = await self._repo.execute(
            """
                SELECT * FROM user_conversion_history WHERE user_id = $1;
            """, user_id
        )

        return MapperUserConversionHistory.to_domain(history)