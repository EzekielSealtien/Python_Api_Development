from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    # 1) on transforme en bytes
    password_bytes = password.encode("utf-8")

    # 2) on SHA256 -> 32 bytes, puis hexdigest -> 64 chars
    digest = hashlib.sha256(password_bytes).hexdigest()

    # 3) bcrypt sur une string courte (64 chars)
    return pwd_context.hash(digest)

def verify_password(plain_password: str, hashed_password: str):
    # 1) on transforme en bytes
    password_bytes = plain_password.encode("utf-8")

    # 2) on SHA256 -> 32 bytes, puis hexdigest -> 64 chars
    digest = hashlib.sha256(password_bytes).hexdigest()

    # 3) bcrypt sur une string courte (64 chars)
    return pwd_context.verify(digest, hashed_password)