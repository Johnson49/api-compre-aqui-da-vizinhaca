from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./api_database.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_bd():
    Base.metadata.create_all(bind=engine)

def session():
    db = SessionLocal()
    try:
        yield db    #return db
    finally:        # e depois finaliza a conexão
        db.close()
