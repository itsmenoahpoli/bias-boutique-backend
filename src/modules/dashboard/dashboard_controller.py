
from fastapi import APIRouter, status
from .dashboard_service import dashboard_service
from src.utils.http_utils import HTTPResponse

dashboard_router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@dashboard_router.get('/summary')
async def get_summary_counts_handler():
    result = dashboard_service.get_summary_counts()
    
    return HTTPResponse(
        detail=result,
        status_code=status.HTTP_200_OK
    )

