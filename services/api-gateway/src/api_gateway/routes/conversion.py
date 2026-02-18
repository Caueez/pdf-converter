import asyncio

from fastapi import APIRouter, Depends, Request, status

from fastapi.responses import JSONResponse

from api_gateway.container import AppContainer

from api_gateway.schemas.conversion import GetConversionJobRequest, CreateConversionJobRequest


router = APIRouter(tags=["Conversion"])


def get_container(request: Request) -> AppContainer:
    return request.app.state.container


@router.post("/conversion")
async def create_conversion_job(
    request: CreateConversionJobRequest,
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.create_conversion_job_use_case.execute(request.conversion_config)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)



@router.get("/conversion/{account_id}")
async def get_conversion_job(
    account_id: GetConversionJobRequest, 
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.get_conversion_job_use_case.execute(account_id)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
