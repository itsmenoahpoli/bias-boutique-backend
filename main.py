from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import initialize_api_routes

app = FastAPI(
	title="Bias Boutique API Server & Database",
	description="Main core data server",
	redoc_url=None
)

app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/payment-status", StaticFiles(directory="public/payment-status"), name="payment-status")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	expose_headers=["*"]
)

initialize_api_routes(app)
