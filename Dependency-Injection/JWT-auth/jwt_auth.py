from datetime import datetime, timezone, timedelta
from authlib.jose import jwt, JoseError
from fastapi import HTTPException

SECRET_KEY = "my_secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    header = {"alg": ALGORITHM}
    expiry = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = data.copy()

    payload.update({"exp": expiry})
    return jwt.encode(header, payload, SECRET_KEY)


def verify_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        username = claims.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token missing username")
        return username

    except JoseError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
