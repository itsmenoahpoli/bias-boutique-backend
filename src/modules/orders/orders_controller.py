import logging
from fastapi import APIRouter, Request, status
from src.modules.payments import payments_service
from .orders_service import orders_service
from .orders_dto import OrderDTO
from src.utils.http_utils import HTTPResponse
from src.constants.errors_constant import ErrorTypes

logging.basicConfig(level=logging.INFO)

orders_router = APIRouter(
	prefix="/orders",
	tags=["Orders"]
)

@orders_router.post('/payments/create-invoice')
async def create_invoice_handler():
	result = payments_service.create_payment_link(500, '[BIAS BOUTIQUE] Test payment', "1")
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_201_CREATED
	)

@orders_router.get('')
async def get_list_handler():
	result = orders_service.get_list_data()
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@orders_router.get('/{id}')
async def get_single_handler(id: str):
	result = orders_service.get_single_data(id)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@orders_router.delete('/{id}')
async def delete_one_handler(id: str):
	result = orders_service.delete_data(id)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)

@orders_router.post('')
async def create_handler(payload: OrderDTO,  request: Request):
	client_ip = request.client.host
	logging.info(f"ORDER CHECKOUT Request received from IP: {client_ip}")
	result = orders_service.create_data(payload.model_dump())

	if result == ErrorTypes.ALREADY_EXISTS:
		return HTTPResponse(
			detail=result,
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
		)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_201_CREATED
	)

@orders_router.get('/by-email/{email}')
async def get_orders_by_email_handler(email: str):
	result = orders_service.get_orders_by_email(email)
	
	return HTTPResponse(
		detail=result,
		status_code=status.HTTP_200_OK
	)
