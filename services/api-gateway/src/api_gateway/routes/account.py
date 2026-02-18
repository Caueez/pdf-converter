import asyncio

from fastapi import APIRouter, Depends, Request, status

from fastapi.responses import JSONResponse

from api_gateway.container import AppContainer

from api_gateway.schemas.account import CreateAccountResquest, GetAccountRequest


router = APIRouter(tags=["Accounts"])


def get_container(request: Request) -> AppContainer:
    return request.app.state.container


@router.post("/account")
async def create_account(
    request: CreateAccountResquest,
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.create_account_use_case.execute(request.name, request.email, request.password)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)



@router.get("/account/{account_id}")
async def get_accounts(
    account_id: GetAccountRequest, 
    container: AppContainer = Depends(get_container)
    ):
    
    try:
        response = await container.get_account_use_case.execute(account_id)
    except Exception as e:
        return JSONResponse(
            content={"message": e},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
