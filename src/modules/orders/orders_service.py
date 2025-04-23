from src.database import entities
from src.modules.base_repository import BaseRepository

class OrdersService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.OrderEntity)
        
        

orders_service = OrdersService()