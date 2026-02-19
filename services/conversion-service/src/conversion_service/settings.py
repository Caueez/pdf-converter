
from pydantic_settings import BaseSettings


from pydantic import BaseModel


class DBConfig(BaseModel):
    host: str
    port: str
    user: str
    password: str
    dbname: str


class MessageringConfig(BaseModel):
    url: str


class RedisConfig(BaseModel):
    host: str
    port: str

class ConversionServiceSettings(BaseSettings):

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "env_nested_delimiter": "__",
    }

    DB_ENV: DBConfig
    CACHE_ENV: RedisConfig
    MESSAGERING_ENV: MessageringConfig