from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from src.routers.router import initialize_api_routes
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
	title="Bias Boutique API Server & Database",
	description="Main core data server",
	redoc_url=None
)

# HTTPS redirect middleware
app.add_middleware(HTTPSRedirectMiddleware)

# CORS middleware configuration
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=False,
	allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH", "HEAD"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=600,  # Cache preflight requests for 10 minutes
)

@app.middleware("http")
async def cors_middleware(request: Request, call_next):
	# Handle preflight requests
	if request.method == "OPTIONS":
		headers = {
			"Access-Control-Allow-Origin": "*",
			"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH, HEAD",
			"Access-Control-Allow-Headers": "*",
			"Access-Control-Max-Age": "600",
		}
		return JSONResponse(content={}, status_code=200, headers=headers)
	
	response = await call_next(request)
	response.headers["Access-Control-Allow-Origin"] = "*"
	return response

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
	logger.info(f"Request: {request.method} {request.url}")
	logger.info(f"Headers: {request.headers}")
	response = await call_next(request)
	logger.info(f"Response status: {response.status_code}")
	return response

# Mount static files after middleware
app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/payment-status", StaticFiles(directory="public/payment-status"), name="payment-status")

initialize_api_routes(app)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
