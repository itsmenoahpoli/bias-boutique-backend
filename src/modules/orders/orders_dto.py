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
    cart_items: List[CartItemDTO]
    total_amount: float
    voucher: Optional[str]
