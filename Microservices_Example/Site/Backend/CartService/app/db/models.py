from sqlalchemy import Table, Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Cart(Base):
    __tablename__ = 'carts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)


class CartProduct(Base):
    __tablename__ = 'cart_products'
    
    cart_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1)
    total = Column(Integer, default=1)


def create_tables(engine) -> None:
    Base.metadata.create_all(bind=engine)