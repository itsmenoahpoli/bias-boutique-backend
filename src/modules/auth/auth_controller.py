from fastapi import APIRouter, status
from .auth_dto import SigninDTO, SignupDTO
from .auth_service import auth_service
from src.utils.http_utils import HTTPResponse
from src.constants.errors_constant import ErrorTypes

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth API"]
)

@auth_router.post('/signin')
def signin_handler(payload: SigninDTO):
    result = auth_service.authenticate_credentials(payload.model_dump())

    if result is False:
        return HTTPResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "message": "Invalid credentials",
                "error": ErrorTypes.UNAUTHORIZED_ERROR
            }
        )

    return HTTPResponse(
        status_code=status.HTTP_200_OK,
        detail={
            "message": "Authentication successful",
            "data": result
        }
    )

@auth_router.post('/signup')
def signup_handler(payload: SignupDTO):
    result = auth_service.signup_account(payload.model_dump())

    if result is False:
        return HTTPResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Account already exists",
                "error": ErrorTypes.ALREADY_EXISTS
            }
        )

    return HTTPResponse(
        status_code=status.HTTP_201_CREATED,
        detail={
            "message": "Account created successfully",
            "data": result
        }
    )
