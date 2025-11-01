from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load .env values
load_dotenv()

user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD", "lakshmi@12")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
db = os.getenv("MYSQL_DB", "librarydb")

# Properly escape special characters in the password (like @, #, $)
safe_password = quote_plus(password)

# ✅ Build the connection URL safely
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{safe_password}@{host}:{port}/{db}"

print("Using DB URL:", SQLALCHEMY_DATABASE_URL)  # debug line; you can remove later

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
