from fastapi import FastAPI

from conversion_service.routers import router

from conversion_service.lifespan import lifespan

def create_app() -> FastAPI:
    app = FastAPI(title="Conversion Service", lifespan=lifespan)
    app.include_router(router)
    return app


app = create_app()

