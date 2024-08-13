from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Magazine(Base):
    __tablename__ = "magazines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    base_price = Column(Float, nullable=False)
    discount_quarterly = Column(Float)
    discount_half_yearly = Column(Float)
    discount_annual = Column(Float)


class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    renewalPeriod = Column(Integer, nullable=False)
    tier = Column(Integer, nullable=False)
    discount = Column(Float, nullable=False)


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    magazine_id = Column(Integer, ForeignKey("magazines.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
    price = Column(Float, nullable=False)
    renewal_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User")
    magazine = relationship("Magazine")
    plan = relationship("Plan")
