from pydantic import BaseModel, Field

class ProductDTO(BaseModel):
	sku: str = Field(min_length=8, max_length=8)
	name: str = Field(min_length=1, max_length=100)
	description: str
	price: float
	discounted_price: float
	stocks_qty: int
	is_discounted: bool
	is_pulished: bool