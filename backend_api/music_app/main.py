from fastapi import FastAPI , Query , Body , Path , Header , Depends
from typing import List , Dict
from enum import Enum
import uvicorn
from pydantic import BaseModel , Field , HttpUrl
from sqlalchemy.orm import Session
from modules import schemas , models
from modules.database import SessionLocal , engine
from routers import landingPageEvents,adminevent,adminphoto,adminuser , admin

app = FastAPI(debug=True)

# models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

# def test(test_param : str = None):
#     return test_param

@app.get('/')
async def root():
    return {"Hello" : "World"}

# THIS IS INCLUDING ALL LANDINGPAGE ENDPOINTS FROM routers/landingPage.py
app.include_router(landingPageEvents.router , prefix="/landingPage" , tags=["landingPage"])  
app.include_router(admin.router , prefix="/admin" , tags=["admin"])  


if __name__ == "__main__":
    uvicorn.run("main:app" , host = "127.0.0.1",port = 8000,reload = True)
