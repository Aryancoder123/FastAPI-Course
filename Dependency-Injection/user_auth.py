from fastapi import FastAPI, Depends, Form, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "Aryan" and password == "Aryan123":
        return {"access_token": "valid_token", "token_type": "bearer"}
    return HTTPException(status_code=400, detail="Invalid useername or password")


def decode_token(token):
    if token == "valid_token":
        return {"name": "Aryan"}
    return HTTPException(
        statuscode=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token"
    )


def get_curr_user(token: str = Depends(OAuth2_scheme)):
    return decode_token(token)


@app.get("/profile")
def get_data(user=Depends(get_curr_user)):
    return {"username": user["name"]}
