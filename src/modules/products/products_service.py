from src.database import entities
from src.modules.base_repository import BaseRepository

class ProductsService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.ProductEntity)
        
        

products_service = ProductsService()