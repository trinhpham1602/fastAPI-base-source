from enum import Enum


# choose int because it helps quickly filter, less space to store
# but developer will be confused because it in-explicit
class ERole(str, Enum):
    admin = 'admin'
    super_user = 'super_user'
    user = 'user'


class ESex(str, Enum):
    male = 'male'
    female = 'female'
    others = 'others'
