import xendit
from src.config.settings import app_settings
import uuid

def create_payment_link(amount: float, description: str):
    # Initialize Xendit client with your secret key
    xendit.api_key = app_settings.app_xendit_secret_key
    
    try:
        # Create an invoice
        invoice = xendit.Invoice.create(
            external_id=str(uuid.uuid4()),  # Generate unique ID for the transaction
            amount=amount,
            description=description,
            currency="PHP",  # Assuming Philippines currency
            success_redirect_url="https://your-success-url.com",  # Replace with your success URL
            failure_redirect_url="https://your-failure-url.com",  # Replace with your failure URL
        )
        
        return {
            "invoice_id": invoice.id,
            "payment_url": invoice.invoice_url,
            "status": invoice.status,
            "amount": invoice.amount
        }
        
    except xendit.XenditError as e:
        return {
            "error": str(e),
            "status": "failed"
        }