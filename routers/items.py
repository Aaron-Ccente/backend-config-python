from fastapi import APIRouter, Depends
from typing import Dict, Union
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models import models
from models.item import model

router = APIRouter(prefix="/items",
                   tags=["items"],
                   responses={404: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()


@router.post("/")
def create_item(item: model.ItemCreate, db: Session = Depends(get_db)) -> Dict[str, Union[str, model.ItemResponse]]:
    item = models.Item(name=item.name, description=item.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return {
    "data": item,
    "message": "item creado correctamente"
    }
