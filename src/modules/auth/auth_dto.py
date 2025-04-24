from pydantic import BaseModel, EmailStr, Field

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
