from sqlalchemy import Table, Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, default="super thing")
    price = Column(String, nullable=False)
    image = Column(String, nullable=False)


def create_tables(engine) -> None:
    Base.metadata.create_all(bind=engine)