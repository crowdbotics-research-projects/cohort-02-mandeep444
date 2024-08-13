from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db

from models import Magazine
from schemas import MagazineSchema

router = APIRouter()


@router.post("/magazines")
def create_magazine(magazine: MagazineSchema, db: Session = Depends(get_db)):
    """
    This method will create a new magazine.
    """
    new_magazine = Magazine(**magazine.dict())
    db.add(new_magazine)
    db.commit()
    db.refresh(new_magazine)
    return new_magazine


@router.get("/magazines")
def get_magazines(db: Session = Depends(get_db)):
        """
        This method will return all the active magazines.
        """
        magazines = db.query(Magazine).filter(Magazine.is_active == True).all()
        return magazines


@router.get("/magazines/{id}")
def get_magazine_by_id(id: int, db: Session = Depends(get_db)):
            """
            This method will return a specific magazine by its ID.
            """
            magazine = db.query(Magazine).filter(Magazine.id == id).first()
            return magazine


@router.delete("/magazines/{id}")
def delete_magazine(id: int, db: Session = Depends(get_db)):
        """
        This method will delete a specific magazine by its ID.
        """
        magazine = db.query(Magazine).filter(Magazine.id == id).first()
        if magazine:
            db.delete(magazine)
            db.commit()
            return {"message": "Magazine deleted successfully"}
        else:
            return {"message": "Magazine not found"}