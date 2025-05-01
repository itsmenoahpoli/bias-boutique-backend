from src.database import entities
from src.modules.base_repository import BaseRepository

class ProductsService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.ProductEntity)
    
    def get_filtered_products(self, category: str = None, name_query: str = None):
        query = {}
        
        if category:
            query["category"] = category
        
        if name_query:
            query["name"] = {"$regex": name_query, "$options": "i"}
        
        result = self._entity.find(query)
        return self._list_serializer(result)

products_service = ProductsService()
