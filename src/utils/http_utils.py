from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
import json
from datetime import datetime

# Configure console logger
console_logger = logging.getLogger("api_logger")
console_logger.setLevel(logging.INFO)

# Remove any existing handlers to avoid duplicate logs
if console_logger.handlers:
    console_logger.handlers.clear()

# Create and configure console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
console_logger.addHandler(console_handler)

# Prevent the logger from propagating to the root logger
console_logger.propagate = False

def HTTPResponse(status_code: status, detail: dict | str):
    response_data = jsonable_encoder(detail)
    
    # Create formatted log message
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "status_code": status_code,
        "response": response_data
    }
    
    formatted_log = json.dumps(log_data, indent=2)
    console_logger.error(status_code)
    
    # Log based on status code
    if status_code >= 400:
        console_logger.error(f"\nAPI Response: {formatted_log}")
    else:
        console_logger.info(f"\nAPI Response: {formatted_log}")
    
    return JSONResponse(
        status_code=status_code,
        content=response_data
    )
