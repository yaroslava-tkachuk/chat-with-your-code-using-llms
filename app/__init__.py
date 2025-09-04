from dotenv import load_dotenv, find_dotenv

from app.config import validate_env


load_dotenv(find_dotenv(usecwd=True))
validate_env()
