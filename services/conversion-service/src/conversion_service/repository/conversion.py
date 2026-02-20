

from infra.database.implementation.repository import DatabaseRepository


class ConversionRepository:
    def __init__(self, repo : DatabaseRepository) -> None:
        self.repo = repo
    
    async def startup(self):
        await self.create_conversion_job_table()
    
    async def create_conversion_job_table(self):
        self.repo.execute(
            """
                CREATE TABLE IF NOT EXISTS conversion_jobs (
                    job_id VARCHAR(255) PRIMARY KEY,
                    status VARCHAR(255),
                    message VARCHAR(255),
                    raw_presigned_url VARCHAR(255),
                    processed_presigned_url VARCHAR(255)
                );
            """
        )


    async def create_conversion_job(self, job_id: str, status: str, message: str, raw_presigned_url: str, processed_presigned_url: str):
        self.repo.execute(
            """
                INSERT INTO conversion_jobs (job_id, status, message, raw_presigned_url, processed_presigned_url)
                VALUES ($1, $2, $3, $4, $5);
            """, 
            job_id, status, message, raw_presigned_url, processed_presigned_url
        )
    
    async def get_conversion_job(self, job_id: str):
        return self.repo.fetch_one(
            """
                SELECT * FROM conversion_jobs WHERE job_id = $1;
            """, 
            job_id
        )