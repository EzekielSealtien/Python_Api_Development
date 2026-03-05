from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app import database, models
from sqlalchemy.orm import Session
from app.database import get_db

ouath2_scheme = OAuth2PasswordBearer(tokenUrl="login")
from app import config

SECRET_KEY=config.settings.SECRET_KEY
ALGORITHM=config.settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("user_id") is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception
    
def get_current_user(token: str=Depends(ouath2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    payload = verify_access_token(token, credentials_exception)
    user=db.query(models.User).filter(models.User.id == payload.get("user_id")).first()

    return user