from fastapi import APIRouter, status
from .auth_dto import SigninDTO, SignupDTO, UpdateAccountDTO
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

@auth_router.post('/update-account/{user_id}')
def update_account_handler(user_id: str, payload: UpdateAccountDTO):
    # If new_password is provided, rename it to password for the service layer
    update_data = payload.model_dump(exclude_none=True)
    if 'new_password' in update_data and update_data['new_password'] is not None:
        update_data['password'] = update_data.pop('new_password')

    result = auth_service.update_account(user_id, update_data)

    if isinstance(result, dict) and "error" in result:
        return HTTPResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": result["error"],
                "error": ErrorTypes.BAD_REQUEST
            }
        )

    return HTTPResponse(
        status_code=status.HTTP_200_OK,
        detail={
            "message": "Account updated successfully",
            "data": result
        }
    )