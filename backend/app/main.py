from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Birthday Reminder App API Working!"}