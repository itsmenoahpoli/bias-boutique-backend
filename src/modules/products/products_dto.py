from pydantic import BaseModel, Field, field_validator
from typing import Optional
from fastapi import HTTPException, status

class ProductDTO(BaseModel):
	sku: str = Field(min_length=8, max_length=8)
	name: str = Field(min_length=1, max_length=100)
	category: str
	description: str
	price: float
	discounted_price: float
	stocks_qty: int
	is_discounted: bool
	is_pulished: bool

	@field_validator('price', 'discounted_price')
	@classmethod
	def validate_prices(cls, value):
		if value < 0:
			raise HTTPException(
				status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
				detail="Price cannot be negative"
			)
		return value

	@field_validator('stocks_qty')
	@classmethod
	def validate_stocks(cls, value):
		if value < 0:
			raise HTTPException(
				status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
				detail="Stock quantity cannot be negative"
			)
		return value


