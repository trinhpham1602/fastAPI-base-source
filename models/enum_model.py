from enum import Enum


# choose int because it helps quickly filter, less space to store
# but developer will be confused because it in-explicit
class ERole(str, Enum):
    admin = 'admin'
    super_user = 'super_user'
    user = 'user'


class ESex(int, Enum):
    male = 1
    female = -1
    others = 0