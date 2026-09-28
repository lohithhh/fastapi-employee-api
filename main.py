from fastapi import FastAPI

from database import Base, engine
from routers.employees import router as employee_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(employee_router)
@app.get("/")
def home():
    return {
        "message": "Employee API is running"
    }