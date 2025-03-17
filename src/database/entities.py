from .connection import get_db_collection

# Users
UserRoleEntity = get_db_collection(collection='user_roles', create_if_none=True)
UserEntity = get_db_collection(collection='users', create_if_none=True)
