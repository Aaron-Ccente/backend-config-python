from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.config import get_db
from models import models
from typing import Dict, Union

router = APIRouter(prefix="/user",
                   tags=["user"],
                   responses={404: {"message": "No encontrado"}})

@router.get("/")
async def get_items(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/name")
async def get_name() -> Dict[str, Union[str, str]]:
    return {'message': 'Hello'}