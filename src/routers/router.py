from fastapi import FastAPI
from src.modules.auth.auth_controller import auth_router
from src.modules.user_roles.user_roles_controller import user_roles_router

API_PREFIX_V1 = "/api/v1"

app_routers = [auth_router, user_roles_router]

def initialize_api_routes(app: FastAPI):
    for router in app_routers:
        app.include_router(router=router, prefix=API_PREFIX_V1)