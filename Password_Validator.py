def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters required")

    if not any(char.isupper() for char in password):
        errors.append("At least one uppercase letter required")

    if not any(char.islower() for char in password):
        errors.append("At least one lowercase letter required")

    if not any(char.isdigit() for char in password):
        errors.append("At least one digit required")

    if not any(char in "!@#$%^&*" for char in password):
        errors.append("At least one special character required")

    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }
print(validate_password("weak"))
print(validate_password("Weak123"))
print(validate_password("MySecure@1"))
