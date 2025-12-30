from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Input model for creating a user. Clients control email and name."""

    email: EmailStr
    name: str


class UserRead(BaseModel):
    """Output model for reading a user. Includes server-managed fields like id and is_active."""

    id: int
    email: EmailStr
    name: str
    is_active: bool
