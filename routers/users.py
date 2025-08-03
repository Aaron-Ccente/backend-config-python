from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models import models

router = APIRouter(prefix="/user",
                   tags=["user"],
                   responses={404: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()