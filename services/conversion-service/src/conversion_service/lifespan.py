from contextlib import asynccontextmanager

from fastapi import FastAPI

from conversion_service.container import AppContainer

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    app.state.container = await AppContainer().startup()
    
    yield

    app.state.container.shutdown()