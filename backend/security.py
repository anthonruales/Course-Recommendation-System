import os
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

load_dotenv()

# --------------- password hashing ---------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# --------------- JWT configuration ---------------
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_IN_PRODUCTION")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a signed JWT containing user_id, username, and is_admin."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Decode and verify a JWT. Raises HTTPException on failure."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# --------------- dependency helpers (used in main.py) ---------------
def _get_db():
    """Lazy import to avoid circular dependency with database module."""
    from database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: Optional[str] = Depends(oauth2_scheme), db: Session = Depends(_get_db)):
    """
    FastAPI dependency — extracts and validates the JWT from the Authorization header.
    Returns the User ORM object.
    Raises 401 if token is missing/invalid, or if the user no longer exists.
    """
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = decode_access_token(token)
    user_id: int = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    import models
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    if hasattr(user, "is_active") and not user.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")
    return user


def require_admin(current_user=Depends(get_current_user)):
    """
    FastAPI dependency — ensures the authenticated user has admin privileges.
    Chain after get_current_user.
    """
    if not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user


def require_self_or_admin(user_id: int, current_user=Depends(get_current_user)):
    """
    FastAPI dependency factory — ensures the authenticated user is either
    accessing their own resource or is an admin.
    """
    if current_user.user_id != user_id and not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=403, detail="Access denied: you can only access your own data")
    return current_user