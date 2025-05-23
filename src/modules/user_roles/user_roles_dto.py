from pydantic import BaseModel, Field

class UserRoleDTO(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	is_enabled: bool