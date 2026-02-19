
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api_gateway.container import AppContainer

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API Gateway is starting...")  

    app.state.container = await AppContainer().startup()
    
    yield
    print("API Gateway is shutting down...")

    await app.state.container.shutdown()

    