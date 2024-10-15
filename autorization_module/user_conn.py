import requests

user_module_url = "http://user_module:8000"

def get_user(user_id: str):
    response = requests.get(f"{user_module_url}/user/{user_id}")
    if response.status_code == 403:
        return {"message": "User is locked"}, True
    return response.json(), False

def lock_user(user_id: str):
    response = requests.post(f"{user_module_url}/user/{user_id}/lock")
    return response.json()

