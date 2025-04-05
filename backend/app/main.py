from fastapi import FastAPI
from .core.database import Base, engine
from .models import user, birthday, reminder_pref
from .routes import birthday_routes, user_routes

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(birthday_routes.router)

@app.get("/")
def read_root():
    return {"msg": "Birthday Reminder API Working!"}