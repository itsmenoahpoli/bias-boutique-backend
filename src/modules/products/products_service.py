from src.database import entities
from src.modules.base_repository import BaseRepository

class ProductsService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.ProductEntity)
    
    def get_filtered_products(self, category: str = None):
        if category:
            result = self._entity.find({"category": category})
        else:
            result = self._entity.find()
        return self._list_serializer(result)

products_service = ProductsService()
