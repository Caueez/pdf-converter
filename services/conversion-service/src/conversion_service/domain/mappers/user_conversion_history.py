
from typing import Any

from conversion_service.domain.entitities.user_conversion_history import UserConversionHistory
from conversion_service.domain.value_objects.plans import Plan, PlanName


class MapperUserConversionHistory:
    @staticmethod
    def to_domain(row) -> UserConversionHistory:
        plan = Plan.create(PlanName(row["plan_name"]))

        return UserConversionHistory(
            user_id = row["user_id"],
            plan = plan,
            active_jobs = row["active_jobs"],
            monthly_jobs = row["monthly_jobs"]
        )