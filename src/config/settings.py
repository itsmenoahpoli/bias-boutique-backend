from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

class AppSettings(BaseSettings):
	app_debug: bool = True
	app_api_key: str
	app_database_db: str
	app_database_url: str

	app_xendit_secret_key: str
	app_xendit_public_key: str

	class Config:
		env_file = '.env'
		env_file_encoding = 'utf-8'
		case_sensitive = False

	@classmethod
	def load_settings(cls):
		load_dotenv(find_dotenv('.env'), override=True)

		return cls()
	
app_settings = AppSettings.load_settings()
