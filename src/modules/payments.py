import xendit
import uuid
from xendit.apis import InvoiceApi
from xendit.invoice.model.create_invoice_request import CreateInvoiceRequest
from src.config.settings import app_settings

xendit.set_api_key(app_settings.app_xendit_secret_key)
client = xendit.ApiClient()

class PaymentsService:
    def create_payment_link(self, amount: float, description: str, order_id: str):
        try:
            amount = float(amount)
            
            response = InvoiceApi(client).create_invoice(
                create_invoice_request=CreateInvoiceRequest(
                    external_id=str(uuid.uuid4()),
                    amount=amount,
                    description=description,
                    currency="PHP",
                    success_redirect_url="http://localhost:8000/payment-status/success.html?order_id=" + order_id,
                    failure_redirect_url="http://localhost:8000/payment-status/failed.html?order_id=" + order_id,
                )
            )

            return {
                "invoice_id": str(response.id),
                "payment_url": str(response.invoice_url),
                "status": str(response.status),
                "amount": float(response.amount),
                "currency": str(response.currency),
                "external_id": str(response.external_id),
                "description": str(response.description),
                "created": str(response.created),
                "expiry_date": str(response.expiry_date) if response.expiry_date else None
            }

        except xendit.XenditSdkException as e:
            print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)
            return {
                "error": str(e),
                "status": "failed"
            }

payments_service = PaymentsService()
