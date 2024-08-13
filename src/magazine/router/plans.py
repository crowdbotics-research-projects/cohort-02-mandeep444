from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db



from models import Plan
from schemas import PlanSchema



router = APIRouter()


@router.get("/plans")
def list_plans(db: Session = Depends(get_db)):
    plans = db.query(Plan).all()
    return plans


@router.put("/plans/{plan_id}")
def edit_plan(plan_id: int, plan: PlanSchema, db: Session = Depends(get_db)):
        existing_plan = db.query(Plan).filter(Plan.id == plan_id).first()
        if existing_plan:
            existing_plan.name = plan.name
            existing_plan.description = plan.description
            db.commit()
            db.refresh(existing_plan)
            return existing_plan
        else:
            return {"message": "Magazine not found"}


@router.delete("/plans/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    existing_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if existing_plan:
        db.delete(existing_plan)
        db.commit()
        return {"message": "Plan deleted successfully"}
    else:
        return {"message": "Plan not found"}