import yaml
import logging
from fastapi import  HTTPException
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
blacklist = set()

def get_user_by_name(user_name: str) -> dict:
    users_path = Path(__file__).parent / "users.yaml"
    with open(users_path) as file:
        users = yaml.safe_load(file)
        users = users["users"]  
    for user in users:
        if user["name"] == user_name:
            if user["name"] in blacklist:
                raise HTTPException(status_code=403, detail="User is locked")
            return user
    return {"error": "User not found"}


def lock_user(user_name: str) -> dict:
    blacklist.add(user_name)
    
def unlock_user(user_name: str) -> dict:
    if user_name in blacklist:
        blacklist.remove(user_name)
        return {"message": "User unlocked"}
    else:
        return {"message": "User not found in blacklist"}
   
