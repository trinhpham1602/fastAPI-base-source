import re
from datetime import datetime


def is_valid_email(email: str):
    if re.match(r'.+@.+\.com$', email):
        return True
    return False


def is_valid_date(date_string, format="%Y-%m-%d"):
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
