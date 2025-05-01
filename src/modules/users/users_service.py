from src.database import entities
from src.modules.base_repository import BaseRepository
from src.utils.password_utils import hash_password
import time

class UsersService(BaseRepository):
    def __init__(self):
        super().__init__(entity=entities.UserEntity)
    
    def find_by_email(self, email):
        user = self._entity.find_one({"email": email})
        if user is None:
            return None
        return self._single_serializer(user)
    
    def find_by_username(self, username):
        user = self._entity.find_one({"username": username})
        if user is None:
            return None
        return self._single_serializer(user)
    
    def find_by_id(self, id):
        user = self._entity.find_one({"_id": id})
        if user is None:
            return None
        return self._single_serializer(user)
    
    def check_user_exists(self, email, username):
        return self.find_by_email(email) is not None or self.find_by_username(username) is not None
    
    def create_user_account(self, account_data):
        account_data['password'] = hash_password(account_data['password'])
        account_data['is_enabled'] = True
        account_data['is_admin'] = False
        account_data['is_verified'] = False
        account_data['is_deleted'] = False
        account_data['createdAt'] = time.time()
        account_data['updatedAt'] = time.time()
        
        return self.create_data(account_data)

    def update_user_account(self, user_id, update_data):
        # If new_password is in update_data, rename it to password
        if "new_password" in update_data:
            update_data["password"] = update_data.pop("new_password")
        
        update_data['updatedAt'] = time.time()
        
        return self.update_data(user_id, update_data)

users_service = UsersService()
