from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABSEURL = "sqlite:///./test.db"

engine = create_engine(
    SQL_ALCHEMY_DATABSEURL, connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
