from pydantic import BaseModel, Field
from typing import Union


class Token(BaseModel):
    access_token: str = Field(
        ..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjU0ODU1MDI1fQ.FOUjiQXkn3diFYKelkQ-_HHHqI6fx4sji6cSDEpQkws")
    expires_in: str = Field(..., example="3600")
    token_type: str = Field(..., example="bearer")


class TokenData(BaseModel):
    username: Union[str, None] = None
