import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import SubscriptionSchema
from models import Subscription

from db import get_db

router = APIRouter()


@router.get("/subscriptions")
def get_active_subscriptions(user_id: int, db: Session = Depends(get_db)):
    """
    This method retrieves all active subscriptions based on user ID.
    """
    subscriptions = (
        db.query(Subscription)
        .filter(Subscription.user_id == user_id, Subscription.is_active == True)
        .all()
    )
    return subscriptions


@router.delete("/subscriptions/{subscription_id}")
def inactivate_subscription(subscription_id: int, db: Session = Depends(get_db)):
    """
    This method inactivates a user's subscription by subscription ID.
    """
    subscription = (
        db.query(Subscription).filter(Subscription.id == subscription_id).first()
    )

    if subscription:
        subscription.is_active = False
        db.commit()
        return {"message": "Subscription inactivated successfully"}
    else:
        return {"message": "Subscription not found"}


@router.post("/subscriptions")
def subscribe_to_magazine(
    subscription: SubscriptionSchema, db: Session = Depends(get_db)
):
    """
    This method subscribes a user to a new magazine plan.
    It calculates the renewal date and price with discount.
    """
    # Calculate renewal date
    current_date = datetime.datetime.now().date()
    renewal_date = current_date + datetime.timedelta(days=subscription.duration)

    # Calculate price with discount
    price = subscription.price
    if subscription.discount:
        price -= (price * subscription.discount) / 100

        # Create new subscription
        new_subscription = Subscription(
            user_id=subscription.user_id,
            magazine_id=subscription.magazine_id,
            renewal_date=renewal_date,
            price=price,
            is_active=True,
        )
        db.add(new_subscription)
        db.commit()

        return {"message": "Subscription created successfully"}
