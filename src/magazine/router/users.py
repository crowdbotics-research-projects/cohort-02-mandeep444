from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from models import User
from schemas import UserSchema



router = APIRouter()


@router.post("/login")
def login(user: UserSchema, db: Session = Depends(get_db)):
    """
    This method will be used to authenticate a user.
    """
    # Check if user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        return {"message": "User does not exist."}
    
    # Check if password is correct
    if existing_user.password != user.password:
        return {"message": "Incorrect password."}
    
    return {"message": "User authenticated successfully."}



@router.post("/register")
def register(user: UserSchema, db: Session = Depends(get_db)):
        """
        This method will be used to register a new user.
        """
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            return {"message": "User already registered."}
        
        # Create a new user
        new_user = User(email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {"message": "User registered successfully."}

@router.post("/logout")
def logout(user: UserSchema, db: Session = Depends(get_db)):
        """
            This method will be used to logout a user.
        """
            # Check if user exists
        existing_user = db.query(User).filter(User.email == user.email).first()
        if not existing_user:
            return {"message": "User does not exist."}
            
        # Perform logout operation
        # For example, you can clear any user session data or tokens here
            
        return {"message": "User logged out successfully."}

@router.post("/resetpassword")
def reset_password(user: UserSchema, db: Session = Depends(get_db)):
    """
            This method will be used to reset the password for a user.
    """
    # Check if user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        return {"message": "User does not exist."}
            
    # Update the user's password
    existing_user.password = user.password
    db.commit()

    return {"message": "Password reset successfully."}
            