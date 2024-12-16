from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 
import os

# take environment variable from.env
load_dotenv()

# connexion a la base de donnée et déclaration de la base avec sql alchemy

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = os.getenv('DB_CONN')

# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# creation d'une session
def get_db():
    """Create a session for the database connection"""
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close
