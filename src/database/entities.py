from .connection import get_db_collection

# Users
UserRoleEntity = get_db_collection(collection='user_roles', create_if_none=True)
UserEntity = get_db_collection(collection='users', create_if_none=True)

# Products
ProductEntity = get_db_collection(collection='products', create_if_none=True)

# Orders
OrderEntity = get_db_collection(collection='orders', create_if_none=True)


