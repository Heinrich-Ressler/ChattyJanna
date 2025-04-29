from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
import re

class TokenData(BaseModel):
    username: str | None = None

class UserCreate(BaseModel):
    username: str
    password: str

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Пароль должен содержать минимум 8 символов")
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", value):
            raise ValueError("Пароль должен содержать буквы, цифры и специальные символы")
        return value

class UserRead(BaseModel):
    id: int
    username: str
    email: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class EmailAdd(BaseModel):
    email: EmailStr

class PasswordConfirm(BaseModel):
    password: str

class UserEdit(BaseModel):
    username: str | None = None