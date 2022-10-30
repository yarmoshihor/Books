
from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos, address
from company import companiapis, dependencies


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
# app.include_router(users.router)
app.include_router(address.router)
app.include_router(
    companiapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={428: {"description": "Internal Use Only"}}
)

