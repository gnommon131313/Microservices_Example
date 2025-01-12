import logging
from sqlalchemy.exc import IntegrityError

from db import models
from db.engine import engine, SessionLocal


def migration_simulation() -> None:
    def init_carts() -> None:
        with SessionLocal() as session:
            carts = [
                # models.Cart(id=1, user_id=666),
                models.Cart(id=2, user_id=777),
                models.Cart(id=3, user_id=888),
            ]
            
            try:
                for cart in carts:
                    session.add(cart)
                
                session.commit()
            except IntegrityError:
                print('ERR: база уже создана 0')
                logging.info('ERR: база уже создана')
                
    def init_cart_products() -> None:
        with SessionLocal() as session:
            cart_products = [
                # models.CartProduct(cart_id=1, product_id=1, quantity=1),
                # models.CartProduct(cart_id=1, product_id=3, quantity=3),
                # models.CartProduct(cart_id=1, product_id=6, quantity=6),
                models.CartProduct(cart_id=2, product_id=8, quantity=4),
                models.CartProduct(cart_id=3, product_id=9, quantity=15),
            ]
            
            try:
                for cart_product in cart_products:
                    session.add(cart_product)
                
                session.commit()
            except IntegrityError:
                print('ERR: база уже создана 1')
                logging.info('ERR: база уже создана')
            
    init_carts()
    init_cart_products()
    
def init() -> None:
    models.create_tables(engine)
    migration_simulation()
    