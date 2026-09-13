import fastapi
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()

user_db = {}


@app.post("/api/users")
def create_user(request: CreateUserRequest) -> UserResponse:
    user_id = len(user_db)+1
    user_db[user_id] = request

    return UserResponse(
        user_id=user_id,
        name=request.name,
        phone_number=request.phone_number,
        height=request.height,
        bio = request.bio
    )


@app.get("/api/users/{user_id}")
def get_user(
    user_id: int = fastapi.Path(
        ...,
        ge=1
    ),
) -> UserResponse:
    if user_id not in user_db:
        raise ValueError("Error : the user id is not existed.")
    
    request = user_db[user_id]
    return UserResponse(
        user_id=user_id, 
        name=request.name,
        phone_number=request.phone_number,
        height=request.height,
        bio = f"{request.bio} 컴퓨터공학과에 재학중인 {request.name}입니다."
    )


@app.get("/api/users")
def get_users(
    min_height: float,
    max_height: float
) -> list[UserResponse]:
    requestList = []

    for i, user in user_db.items():
        user = user_db[i]
        if min_height <= user.height <= max_height:
            userDTO = UserResponse(
                user_id=i,
                name=user.name,
                phone_number=user.phone_number,
                height=user.height,
                bio=user.bio
                )
            requestList.append(userDTO)
    
    return requestList