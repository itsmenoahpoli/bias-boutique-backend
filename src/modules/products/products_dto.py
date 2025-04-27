from pydantic import BaseModel, Field
from fastapi import Form, UploadFile, File
from typing import Annotated

class ProductCreateDTO:
    def __init__(
        self,
        name: Annotated[str, Form()],
        category: Annotated[str, Form()],
        description: Annotated[str, Form()],
        price: Annotated[float, Form()],
        stock: Annotated[int, Form()],
        image: Annotated[UploadFile, File()]
    ):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.stock = stock
        self.image = image


