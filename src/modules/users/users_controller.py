from fastapi import APIRouter, status
from .users_service import users_service
from src.utils.http_utils import HTTPResponse

users_router = APIRouter(
	prefix="/users",
	tags=["Users"]
)

@users_router.get('/')
async def get_list_handler():
	result = users_service.get_list_data()
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@users_router.get('/{id}')
async def get_single_handler(id: str):
	result = users_service.get_single_data(id)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)