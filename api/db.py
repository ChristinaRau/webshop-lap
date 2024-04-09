from .config import DB_URI
from sqlalchemy import create_engine

engine = create_engine(DB_URI, echo=True, pool_pre_ping=True)
