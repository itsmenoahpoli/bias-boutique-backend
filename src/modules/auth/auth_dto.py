from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SigninDTO(BaseModel):
	email: EmailStr
	password: str = Field(min_length=8, max_length=32)


class SignupDTO(BaseModel):
	name: str
	username: str
	contact_no: str
	email: EmailStr
	password: str = Field(min_length=8, max_length=32)
	account_type: str


class UpdateAccountDTO(BaseModel):
	name: str
	email: EmailStr
	contact_number: str
	address: str
	new_password: Optional[str] = Field(min_length=8, max_length=32, default=None)
