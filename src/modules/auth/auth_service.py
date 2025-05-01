import time
import jwt
from bson import ObjectId  # Import ObjectId for MongoDB
from src.config.settings import app_settings
from src.modules.users.users_service import users_service
from src.utils.password_utils import verify_password, hash_password

TOKEN_EXPIRATION_TIME = time.time() + 86400

class AuthService:
	__JWT_SECRET_KEY = app_settings.app_api_key

	def __check_user_credentials(self, credentials):
		user = users_service.find_by_email(credentials['email'])

		print(verify_password(credentials['password'], user['password']))

		if user is None or user['is_enabled'] is False or verify_password(credentials['password'], user['password']) is False:
			return False
		
		return user

	def authenticate_credentials(self, credentials):
		user = self.__check_user_credentials(credentials)

		if user is False:
			return False

		auth_encode = {
			"user": {
				"id": user['id'],
				"name": user['name'],
				"email": user['email'],
				"account_type": user['account_type']
			},
			"expires": TOKEN_EXPIRATION_TIME
		}
		token = jwt.encode(auth_encode, self.__JWT_SECRET_KEY, algorithm="HS256")

		return {
			"user": auth_encode["user"],
			"token": token
		}
	
	def signup_account(self, account_data):
		check_user = users_service.check_user_exists(account_data['email'], account_data['username'])

		if check_user:
			return False

		account_data['password'] = account_data['password']
		users_service.create_user_account(account_data)

		return "ACCOUNT_CREATED"

	def update_account(self, user_id, update_data):
		if not ObjectId.is_valid(user_id):
			return {"error": "Invalid user ID"}

		user = users_service.find_by_id(ObjectId(user_id))
		if not user:
			return {"error": "User not found"}

		if "new_password" in update_data:
			update_data["new_password"] = hash_password(update_data["new_password"])

		updated_user = users_service.update_user_account(ObjectId(user_id), update_data)
		if updated_user:
			return {"message": "Account updated successfully"}
		else:
			return {"error": "Failed to update account"}

auth_service = AuthService()
