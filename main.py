from fastapi import FastAPI
from src.database.db import session
from src.routers.user import Users
from src.models.user import User 

app = FastAPI(title="Colsenet", summary="Colsenet")

app.include_router(Users.router)

@app.get("/")
async def root():
    return {"message": "Colsenet"}

#uvicorn main:app --reload