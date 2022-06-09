from pickle import FALSE
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import users
from app.routes.auth import token
from app.routes.customers import vulnerableCustomerEvents

app = FastAPI()

# app.include_router(
#    users.router,
#    tags=["Users"],
#    prefix="/users"
# )

app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)

app.include_router(
    token.router,
    tags=["OAuth Token"],
    prefix=""
)

app.include_router(
    vulnerableCustomerEvents.router,
    tags=["Customer Vulnerable Events"],
    prefix="/customers"
)
