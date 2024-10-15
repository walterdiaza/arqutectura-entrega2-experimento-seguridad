from fastapi import FastAPI
from user_module.user_handler import get_user_by_name, lock_user, unlock_user

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    return get_user_by_name(user_id)

@app.post("/user/{user_id}/lock")
async def lock_user_ep(user_id: str):
    return lock_user(user_id)

@app.post("/user/{user_id}/unlock")
async def unlock_user_ep(user_id: str):
    return unlock_user(user_id)
    
    
    
