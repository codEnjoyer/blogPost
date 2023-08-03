from fastapi_users import BaseUserManager, IntegerIDMixin

from users.models import User


# TODO: Добавить свой функционал по необходимости
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    pass
