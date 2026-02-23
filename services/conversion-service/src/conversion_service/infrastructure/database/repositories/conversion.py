

from infra.database.implementation.repository import DatabaseRepository

from conversion_service.domain.entitities.conversion_job import ConversionJob

from conversion_service.domain.mappers.conversion_job import MapperConversionJob

from conversion_service.application.ports.repositories.conversion_job import ConversionJobRepositoryInterface

class ConversionJobRepository(ConversionJobRepositoryInterface):
    def __init__(self, repo : DatabaseRepository) -> None:
        self._repo = repo    
    
    async def create_conversion_job(self, conversion_job: ConversionJob):
        await self._repo.execute(
            """
                INSERT INTO conversion_jobs (job_id, status, bucket_name, storage_key)
                VALUES ($1, $2, $3, $4);
            """, 
            conversion_job.job_id, conversion_job.status, conversion_job.bucket_name, conversion_job.storage_key
        )
    
    async def get_conversion_job(self, job_id: str):
        if not job_id:
            raise Exception("Job id is required")

        conversion_job = await self._repo.fetch_one(
            """
                SELECT * FROM conversion_jobs WHERE job_id = $1;
            """, 
            job_id
        )
        if conversion_job:
            return MapperConversionJob.to_domain(conversion_job)