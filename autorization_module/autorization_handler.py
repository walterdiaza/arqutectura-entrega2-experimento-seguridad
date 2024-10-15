import yaml
from pathlib import Path
from autorization_module.user_conn import get_user, lock_user
import json
from fastapi import HTTPException

import logging
logging.basicConfig(level=logging.DEBUG)


def validate_user_permission(user_id: str, permission_id: str) -> bool:  
    user_permission = get_user_permission(user_id)
    logging.info(user_permission)
    
    if permission_id in user_permission["permission_list"]:
        return True
    else:
        lock_user(user_id)
        raise HTTPException(403, "The user does not have permmison, the user was locked")
    
def get_user_permission(user_id: str):
    users_path = Path(__file__).parent / "roles.yaml"
    with open(users_path) as file:
        roles = yaml.safe_load(file)
    user, is_block = get_user(user_id)
    
    if is_block:
        raise HTTPException(403,"The user is locked")    
    
    user_rol = user["role"]
    user_permission = set(roles[user_rol]["permissions"])
    logging.info(user_permission)
    
    return {"permission_list": list(user_permission)}
    
        
        
