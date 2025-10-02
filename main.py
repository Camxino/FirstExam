from fastapi import FastAPI, Path
from models.user import User
import string
import itertools

app = FastAPI()

user = [
    {
        "id": 1,
        "username": "username",
        "password": "password123",
        "email": "email",
        "is_active": True
    }
]

def fuerza_bruta(contrañesa_objetivo):
    caracteres = string.ascii_letters + string.digits
    intentos = 0
    print("Iniciando ataque de contraseña...")
    
    for longitud in range(1, 20):
        for intento in map(''.join, itertools.product(caracteres, repeat=longitud)):
            intentos += 1
            if intento == contrañesa_objetivo:
                print(f"Contraseña encontrada: {intento}")
                print(f"He tardado: {intentos} intentos")
                return
    print("No se ha encontrado la contraseña")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/user")
def get_users():
    return user

@app.get("/user/{user_id}")
def get_user(id: int = Path(gt=0)):
    return list(filter(lambda item: item["id"] == id, user)) 

@app.post("/user")
def create_user(users: User):
    user.append(users.dict())
    fuerza_bruta(users.password)
    return user

@app.put("/user/{user_id}")
def update_user(id: int, user: User):
    for index, item in enumerate(user):
        if item["id"] == id:
            user[index]["username"] = user.username
            user[index]["email"] = user.email
    return user

@app.delete("/user/{user_id}")
def delete_user(id: int):
    for item in user:
        if item["id"] == id:
            user.remove(item)
    return user

@app.post("/login")
def create_login(username: str, password: str):
    for item in user:
        if item["username"] == username and item["password"] == password:
            return {"message": "Login successful"}
    return {"message": "Login failed"}



