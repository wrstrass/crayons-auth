import os
from dotenv import load_dotenv

load_dotenv()


PREFIX = "/api/v1"

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ACCESS_EXPIRE_TIME = int(os.getenv("JWT_ACCESS_EXPIRE_TIME"))
JWT_REFRESH_EXPIRE_TIME = int(os.getenv("JWT_REFRESH_EXPIRE_TIME"))

DB = os.getenv("DB")
DB_DRIVER = os.getenv("DB_DRIVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
