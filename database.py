from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:24data@localhost:5432/demo",
                echo=True)

Base = declarative_base()
Session = sessionmaker()