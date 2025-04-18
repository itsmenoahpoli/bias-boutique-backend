from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.router import initialize_api_routes

app = FastAPI(
	title="Bias Boutique API Server & Database",
	description="Main core data server",
	redoc_url=None
)

app.add_middleware(
  CORSMiddleware,
	allow_origins=['*'],
	allow_methods=["*"],
	allow_headers=["*"],
)

initialize_api_routes(app)