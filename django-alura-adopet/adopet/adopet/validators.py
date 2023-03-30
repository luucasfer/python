from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def validateName(name):
    return name.isalpha()

