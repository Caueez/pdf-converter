
from dataclasses import dataclass

from conversion_service.domain.value_objects.plans import Plan, PlanName

@dataclass
class UserConversionHistory:
    user_id: str
    plan: Plan
    active_jobs: int
    monthly_jobs: int

    @classmethod
    def create(cls, user_id: str):
        return cls(
            user_id = user_id,
            plan = Plan.create(PlanName.FREE),
            active_jobs = 0,
            monthly_jobs = 0
        )
    
    def can_upload(self) -> None:
        """
        Check if the user can upload a new conversion job
        """
        if self.active_jobs >= self.plan.limit_active_jobs:
            raise Exception(f"{self.plan.name} plan can't have more than {self.plan.limit_active_jobs} active jobs")
        
        if self.monthly_jobs >= self.plan.limit_monthly_jobs:
            raise Exception(f"{self.plan.name} plan can't have more than {self.plan.limit_monthly_jobs} jobs per month")

    
    def add_active_job(self):
        self.active_jobs += 1
    
    def remove_active_job(self):
        if self.active_jobs == 0:
            raise Exception("No active jobs to remove")
        self.active_jobs -= 1

    def add_monthly_job(self):
        self.monthly_jobs += 1
    
    def reset_monthly_jobs(self):
        self.monthly_jobs = 0