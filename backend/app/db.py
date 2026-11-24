import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("../.env")

engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
Session = sessionmaker(bind=engine, expire_on_commit=False)