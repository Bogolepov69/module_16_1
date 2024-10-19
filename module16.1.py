from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Hello World")


@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_page(user_id: int = Path(..., gt=0)):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def user_info(username: str = Query(..., description="Имя пользователя"),
                    age: int = Query(..., gt=0, description="Возраст пользователя")):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
