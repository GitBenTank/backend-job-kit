from fastapi import APIRouter, HTTPException, status

from app.models.user import UserCreate, UserRead

router = APIRouter()

# In-memory storage (dict for O(1) lookup by ID)
# This is acceptable for Day 2 - persistence comes later
users_db: dict[int, UserRead] = {}
next_id: int = 1


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def create_user(user: UserCreate) -> UserRead:
    """
    Create a new user.

    Pydantic automatically validates:
    - Email format (EmailStr)
    - Required fields
    - Type correctness
    """
    global next_id

    # Check for duplicate email (simple validation)
    for existing_user in users_db.values():
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
            )

    # Create user with server-managed fields
    new_user = UserRead(id=next_id, email=user.email, name=user.name, is_active=True)

    users_db[next_id] = new_user
    next_id += 1

    return new_user


@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int) -> UserRead:
    """
    Get a user by ID.

    Returns 404 if user doesn't exist.
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found"
        )

    return users_db[user_id]
