from pydantic import BaseModel, field_validator
import re

class CreateUserRequest(BaseModel):
    name: str 
    phone_number: str
    height: float
    bio: str | None = None
    
    @field_validator('phone_number', mode='before')
    @classmethod
    def check_phonenum(cls, v: str) -> str:
        if isinstance(v, str) and re.fullmatch(r"010-\d{4}-\d{4}", v):
            return v
        raise ValueError(f"입력하신 전화번호 {v} 는 010-XXXX-XXXX 형식에 맞지 않습니다.")

    @field_validator("height", mode="before")
    @classmethod
    def check_height_type(cls, v: object) -> object:
        if isinstance(v, str):
            raise ValueError("height는 숫자여야 합니다.")
        return v

    @field_validator("bio")
    @classmethod
    def check_bio_length(cls, v: str | None) -> str | None:
        if v is not None and len(v) > 500:
            raise ValueError("bio는 500자를 초과할 수 없습니다.")
        return v


class UserResponse(BaseModel):
    user_id: int
    name: str
    phone_number: str
    height: float
    bio: str | None = None