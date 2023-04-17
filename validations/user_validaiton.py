import re
def is_valid_email(email: str):
    if re.match(r'.+@.+\.com$', email):
        return True
    return False
