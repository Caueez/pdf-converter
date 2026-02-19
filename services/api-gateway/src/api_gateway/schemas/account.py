from pydantic import BaseModel


class CreateAccountResquest(BaseModel):
    name: str
    email: str
    password: str

class GetAccountRequest(BaseModel):
    id: str