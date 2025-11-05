from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.db.session import get_db
from app.models.users import User
from app.schemas.user_schema import UserCreate, UserOut

router = APIRouter()


@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    Common causes of POST failure:
    - Missing required fields (username, first_name, password_hash)
    - Unique constraint violations on email/phone/username
    - Foreign key constraint (role_code pointing to non-existent Role)
    - DB connectivity issues

    This endpoint catches IntegrityError and returns a 400 with a helpful message.
    """
    new_user = User(**user.dict())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        # Return a friendly client error; exact field not parsed here
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with provided email/phone/username or role already exists / invalid",
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while creating user",
        )

# Ensure router is exported
__all__ = ['router']
