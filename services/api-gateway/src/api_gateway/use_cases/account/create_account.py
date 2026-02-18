


class CreateAccountUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, name: str, email: str, password: str):
        
        return {"message": "Account created"}