from fastapi import FastAPI
from autorization_module.autorization_handler import validate_user_permission, get_user_permission

app = FastAPI()

user_module_url = "user_module:8000"

@app.get("/user/{user_id}/permission/{permission_id}")
async def get_user_authorization(user_id: str, permission_id: str):
    valid_user = validate_user_permission( user_id, permission_id)
    if valid_user:
        return {"message": "User has permission"}


@app.get("/user/{user_id}/permission") 
async def get_user_permission_list(user_id: str):
    return get_user_permission(user_id)
    


