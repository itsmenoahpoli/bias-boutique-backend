from fastapi import APIRouter, status, File, UploadFile, Depends, Form, Query, Body
from .products_service import products_service
from .products_dto import ProductCreateDTO
from src.utils.http_utils import HTTPResponse
from src.utils.file_utils import save_upload_file
from src.constants.errors_constant import ErrorTypes
from typing import Optional, Annotated
from pydantic import BaseModel

# Add this new ProductUpdateDTO class
class ProductUpdateDTO(BaseModel):
    name: str
    category: str
    description: str
    price: float
    stock: int

products_router = APIRouter(
	prefix="/products",
	tags=["Products"]
)

@products_router.get('')
async def get_list_handler(category: Optional[str] = Query(None, description="Filter products by category")):
	result = products_service.get_filtered_products(category)
	
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

@products_router.post('')
async def create_handler(
    name: Annotated[str, Form()],
    category: Annotated[str, Form()],
    description: Annotated[str, Form()],
    price: Annotated[float, Form()],
    stock: Annotated[int, Form()],
    image: Optional[UploadFile] = File(None)
):
    product_data = {
        "name": name,
        "category": category,
        "description": description,
        "price": price,
        "stock": stock,
        "image": "/assets/products/default-product.jpg"  # Default image path
    }
    
    if image:
        if not image.content_type.startswith('image/'):
            return HTTPResponse(
                detail="File must be an image",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        UPLOAD_DIR = "public/assets/products"
        saved_filename = save_upload_file(image, UPLOAD_DIR)
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

@products_router.put('/{id}')
async def update_handler(
    id: str,
    payload: ProductUpdateDTO  # Changed to use the DTO instead of Form fields
):
    product_data = payload.model_dump()  # Convert Pydantic model to dict
    
    result = products_service.update_data(id, product_data)

    if result is None:
        return HTTPResponse(
            detail=ErrorTypes.NOT_FOUND_ERROR,
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    return HTTPResponse(
        detail=result,
        status_code=status.HTTP_200_OK
    )
