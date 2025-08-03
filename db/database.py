from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión: mysql+pymysql://usuario:contraseña@host:puerto/base
DATABASE_URL = "mysql+pymysql://root:Ccentejuan06%40@localhost:3306/serverpython"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()