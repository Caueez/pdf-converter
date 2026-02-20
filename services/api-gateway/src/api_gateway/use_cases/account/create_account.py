
<<<<<<< HEAD
from infra.http.interface.http import HttpInterface

class CreateAccountUseCase:
    def __init__(self, http_client : HttpInterface) -> None:
        self.http_client = http_client

    async def execute(self, name: str, email: str, password: str):
        try:
            response = await self.http_client.post(f"http://account-service:8000/account/", data={"name": name, "email": email, "password": password})
            return response
        except Exception as e:
            raise Exception(e)
=======


class CreateAccountUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, name: str, email: str, password: str):
        
        return {"message": "Account created"}
>>>>>>> 169784b (partial: api-gateway service implementation)
