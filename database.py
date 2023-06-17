import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

engine = create_engine(f"{DATABASE_URL}/{DATABASE_NAME}")

# Create the database if it doesn't exist
if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database {DATABASE_NAME} created.")
