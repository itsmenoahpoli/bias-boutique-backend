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
        
        payment_result = payments_service.create_payment_link(
            amount=data['total_amount'],
            description=f"[BIAS BOUTIQUE] Order #{order_number} payment for {data['customer_email']}",
            order_id=str(order_number)
        )
        
        if payment_result.get('error'):
            return {
                'error': payment_result['error'],
                'status': 'failed'
            }
        
        data['cart_items'] = json.dumps(data['cart_items'])
        data['payment_link'] = payment_result['payment_url']
        data['payment_status'] = payment_result['status']
        data['is_paid'] = False
        data['date_checkout'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['payment_type'] = 'online'
        data['date_paid'] = None

        print(data)
        
        return super().create_data(data, flag_unique_by)

orders_service = OrdersService()
