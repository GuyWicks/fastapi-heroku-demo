from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.models.token import Token
from app.models.user import authenticate_user, fake_users_db, create_access_token, ACCESS_TOKEN_EXPIRE_SECONDS, timedelta

router = APIRouter()


@router.post("/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.client_id:
        user = authenticate_user(
            fake_users_db, form_data.client_id, form_data.client_secret)
    else:
        user = authenticate_user(
            fake_users_db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "expires_in": ACCESS_TOKEN_EXPIRE_SECONDS,
        "token_type": "bearer"
    }
