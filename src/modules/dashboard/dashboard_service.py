
from src.database import entities
from src.modules.base_repository import BaseRepository

class DashboardService(BaseRepository):
    def __init__(self):
        self.product_entity = entities.ProductEntity
        self.order_entity = entities.OrderEntity
        self.user_entity = entities.UserEntity
    
    def get_summary_counts(self):
        products_count = self.product_entity.count_documents({})
        orders_count = self.order_entity.count_documents({})
        customers_count = self.user_entity.count_documents({"account_type": "customer"})
        
        return {
            "total_products": products_count,
            "total_orders": orders_count,
            "total_customers": customers_count
        }

dashboard_service = DashboardService()

