from fastapi import FastAPI
from routes.user import user
app = FastAPI()   #calls the api
app.include_router(user)