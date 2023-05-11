from fastapi import HTTPException, status
from error_messages import INCORRECT_USERNAME_PASSWORD
import repository.user_repository as user_repo


async def get_user_by_email(email: str, password: str):
    user = await user_repo.get_user_by_email(email)
    if not user or not user.is_match_password(password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=INCORRECT_USERNAME_PASSWORD)
