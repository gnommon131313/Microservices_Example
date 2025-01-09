import logging
from sqlalchemy.exc import IntegrityError
from db import models
from db.engine import engine, SessionLocal


# Симуляция миграции
def init() -> None:
    models.create_tables(engine)
    
    with SessionLocal() as session:
        products = [
            models.Product(name="thing 1", description = "super", price=11.0, image=f"Egg.png"),
            models.Product(name="thing 2", description = "super", price=22.0, image=f"EggRaw.png"),
            models.Product(name="thing 3", description = "super", price=33.0, image=f"EggsFried.png"),
            models.Product(name="thing 4", description = "super", price=44.0, image=f"Fish.png"),
            models.Product(name="thing 5", description = "super", price=55.0, image=f"FishCut.png"),
            models.Product(name="thing 6", description = "super", price=66.0, image=f"FishFried.png"),
            models.Product(name="thing 7", description = "super", price=77.0, image=f"FishSkeleton.png"),
            models.Product(name="thing 8", description = "super", price=88.0, image=f"FriedMeat.png"),
            models.Product(name="thing 9", description = "super", price=99.0, image=f"GarbageBag.png"),
            models.Product(name="thing 10", description = "super", price=100.0, image=f"Meat.png"),
            models.Product(name="thing 11", description = "super", price=111.0, image=f"MeatCut.png"),
            models.Product(name="thing 12", description = "super", price=122.0, image=f"PiecesOfMeat.png"),
            models.Product(name="thing 13", description = "super", price=133.0, image=f"XX.png"),
            models.Product(name="thing 14", description = "super", price=144.0, image=f"XX.png"),
            models.Product(name="thing 15", description = "super", price=155.0, image=f"XX.png"),
            models.Product(name="thing 16", description = "super", price=166.0, image=f"XX.png"),
        ]
        
        try:
            for product in products:
                session.add(product)
            
            session.commit()
        except IntegrityError:
            print('ERR: база уже создана')
            logging.info('ERR: база уже создана')
    