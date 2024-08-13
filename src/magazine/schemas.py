from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str

class MagazineSchema(BaseModel):
    name: str
    description: str
    base_price: float

class PlanSchema(BaseModel):
    title: str
    description: str
    renewalPeriod: int
    tier: int
    discount: float

class SubscriptionSchema(BaseModel):
    user_id: int
    magazine_id: int
    plan_id: int
    price: float
    renewal_date: str
    is_active: bool