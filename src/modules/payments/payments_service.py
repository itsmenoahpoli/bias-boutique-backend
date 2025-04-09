from pprint import pprint
from src.config.settings import app_settings
import base64

def generate_auth_header():
    auth_string = f"{app_settings.app_xendit_secret_key}:"
    
    auth_bytes = auth_string.encode('ascii')
    base64_auth = base64.b64encode(auth_bytes).decode('ascii')
    
    return {
        'Authorization': f'Basic {base64_auth}'
    }

def create_payment_link():
    pass