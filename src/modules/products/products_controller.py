from fastapi import APIRouter, status
from .products_service import products_service
from .products_dto import ProductDTO
from src.utils.http_utils import HTTPResponse
from src.constants.errors_constant import ErrorTypes

products_router = APIRouter(
	prefix="/products",
	tags=["Products"]
)

@products_router.get('/')
async def get_list_handler():
	result = products_service.get_list_data()
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@products_router.get('/{id}')
async def get_single_handler(id: str):
	result = products_service.get_single_data(id)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@products_router.delete('/{id}')
async def delete_one_handler(id: str):
	result = products_service.delete_data(id)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@products_router.post('/')
async def create_list_handler(payload: ProductDTO):
	result = products_service.create_data(payload.model_dump(), 'name')

	if result == ErrorTypes.ALREADY_EXISTS:
		return HTTPResponse(
			detail=result,
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
		)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_201_CREATED
	)