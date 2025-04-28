from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import initialize_api_routes
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
	title="Bias Boutique API Server & Database",
	description="Main core data server",
	redoc_url=None,
	redirect_slashes=False
)


# CORS middleware configuration
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173", "https://biasboutiquedashboard.up.railway.app"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=600,
)

# Mount static files after middleware
app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/payment-status", StaticFiles(directory="public/payment-status"), name="payment-status")

initialize_api_routes(app)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)
