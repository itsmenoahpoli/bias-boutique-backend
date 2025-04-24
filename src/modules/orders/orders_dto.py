from pydantic import BaseModel, Field
from typing import Optional, List

class CartItemDTO(BaseModel):
    sku: str
    name: str
    quantity: int
    price: float
    total: float

class OrderDTO(BaseModel):
    customer_email: str
    payment_link: str
    cart_items: List[CartItemDTO]
    total_amount: float
    voucher: Optional[str]
    is_paid: bool
    date_checkout: str
    payment_type: str
    date_paid: Optional[str]
