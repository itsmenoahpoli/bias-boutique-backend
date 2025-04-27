from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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

# Explicit OPTIONS handler for all routes
@app.options("/{full_path:path}")
async def options_handler(request: Request):
	return JSONResponse(
		status_code=200,
		content={"message": "OK"},
	)

# CORS middleware configuration
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=False,  # Must be False when using allow_origins=["*"]
	allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=3600,
)

@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
	response = await call_next(request)
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH"
	response.headers["Access-Control-Allow-Headers"] = "*"
	return response

# Mount static files after middleware
app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/payment-status", StaticFiles(directory="public/payment-status"), name="payment-status")

initialize_api_routes(app)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)
