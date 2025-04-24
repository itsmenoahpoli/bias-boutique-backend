from fastapi import APIRouter, status, File, UploadFile, Depends, Form
from .products_service import products_service
from .products_dto import ProductDTO
from src.utils.http_utils import HTTPResponse
from src.utils.file_utils import save_upload_file
from src.constants.errors_constant import ErrorTypes
import json

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
async def create_handler(
	payload: str = Form(...),
	image: UploadFile = File(..., description="Product image file")
):
	if not image.content_type.startswith('image/'):
		return HTTPResponse(
			detail="File must be an image",
			status_code=status.HTTP_400_BAD_REQUEST
		)
	
	product_data = json.loads(payload)
	product_dto = ProductDTO(**product_data)
	
	UPLOAD_DIR = "public/assets/products"
	saved_filename = save_upload_file(image, UPLOAD_DIR)
	
	product_data = product_dto.model_dump()
	product_data['image'] = f"/assets/products/{saved_filename}"
	
	result = products_service.create_data(product_data, 'name')

	if result == ErrorTypes.ALREADY_EXISTS:
		return HTTPResponse(
			detail=result,
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
		)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_201_CREATED
	)
