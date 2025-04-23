from pydantic import BaseModel, Field
from typing import Optional

class OrderDTO(BaseModel):
	customer_email: str = Field(min_length=8, max_length=8)
	payment_link: str
	cart_items: str
	total_amount: float
	voucher: Optional[str]
	is_paid: bool
	date_checkout: str
	date_paid: Optional[str]