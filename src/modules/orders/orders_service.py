import json
from datetime import datetime
from src.database import entities
from src.modules.base_repository import BaseRepository
from src.modules.payments import payments_service

class OrdersService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.OrderEntity)
    
    def generate_order_number(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f"ORD{timestamp}"
    
    def create_data(self, data, flag_unique_by=None):
        order_number = self.generate_order_number()
        data['order_number'] = order_number
        
        # payment_result = payments_service.create_payment_link(
        #     amount=data['total_amount'],
        #     description=f"[BIAS BOUTIQUE] Order #{order_number} payment for {data['customer_email']}",
        #     order_id=str(order_number)
        # )
        
        # if payment_result.get('error'):
        #     return {
        #         'error': payment_result['error'],
        #         'status': 'failed'
        #     }
        
        data['cart_items'] = json.dumps(data['cart_items'])
        data['payment_link'] = None
        data['payment_status'] = "pending"
        data['is_paid'] = False
        data['date_checkout'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['payment_type'] = 'online'
        data['shipping_status'] = 'to-ship'
        data['date_paid'] = None

        print(data)
        
        return super().create_data(data, flag_unique_by)

    def get_orders_by_email(self, email):
        orders = self._entity.find({"customer_email": email})
        return self._list_serializer(orders)

orders_service = OrdersService()
