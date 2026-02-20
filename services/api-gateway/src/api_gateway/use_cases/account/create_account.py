
from infra.http.interface.http import HttpInterface

class CreateAccountUseCase:
    def __init__(self, http_client : HttpInterface) -> None:
        self.http_client = http_client

    async def execute(self, name: str, email: str, password: str):
        try:
            response = await self.http_client.post(f"http://account-service:8000/account/", data={"name": name, "email": email, "password": password})
            return response
        except Exception as e:
<<<<<<< HEAD
            raise Exception(e)
=======
            raise Exception(e)
>>>>>>> 1a86441 (partial: implement http_client)
