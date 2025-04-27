from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import initialize_api_routes

app = FastAPI(
	title="Bias Boutique API Server & Database",
	description="Main core data server",
	redoc_url=None
)

# Define allowed origins - add your frontend URLs here
origins = [
	"http://localhost:5173",  # Vite default
	"http://localhost:3000",
	"https://bias-boutique-backend-production.up.railway.app",
	"*"  # Allow all origins
]

# Add CORS middleware before mounting static files
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],  # Explicit methods
	allow_headers=["Content-Type", "Authorization", "Accept", "Origin", "X-Requested-With"],
	expose_headers=["*"],
	max_age=3600,  # Cache preflight requests for 1 hour
)

app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")
app.mount("/payment-status", StaticFiles(directory="public/payment-status"), name="payment-status")

initialize_api_routes(app)
