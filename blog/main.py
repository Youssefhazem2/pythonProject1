from fastapi import FastAPI, Depends
import models
import scemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"name": "First Data"}


@app.post("/blog")
def creat(request: scemas.Blog, db: Session = Depends(get_bd)):
    return request
