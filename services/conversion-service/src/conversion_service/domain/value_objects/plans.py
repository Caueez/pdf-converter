from dataclasses import dataclass
from enum import Enum


class PlanName(Enum):
    FREE = "free"
    PRO = "pro"

@dataclass(frozen=True)
class Plan:
    name: PlanName
    limit_active_jobs: int
    limit_monthly_jobs: int

    @staticmethod
    def create(name: PlanName) -> "Plan":
        limits = {
            PlanName.FREE: (3, 100),
            PlanName.PRO: (15, 500),
        }

        if name not in limits:
            raise ValueError("Invalid plan")

        active, monthly = limits[name]

        return Plan(
            name=name,
            limit_active_jobs=active,
            limit_monthly_jobs=monthly
        )