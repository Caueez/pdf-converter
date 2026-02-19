import asyncio

from fastapi import APIRouter, Depends, Request, status

from fastapi.responses import JSONResponse

from conversion_service.container import AppContainer

from conversion_service.schemas.conversion import APIGatewayPayload


router = APIRouter(tags=["Conversion"])


def get_container(request: Request) -> AppContainer:
    return request.app.state.container


@router.post("/create_conversion_job")
async def create_conversion_job(
    payload: APIGatewayPayload,
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.create_conversion_job_use_case.execute(payload.conversion_config)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)



@router.get("/get_conversion_job")
async def get_conversion_job(
    payload: APIGatewayPayload, 
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.get_conversion_job_use_case.execute(payload)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
