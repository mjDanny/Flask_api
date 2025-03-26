from marshmallow import Schema, fields, validate
import re

# Кастомная валидация логина: только латинские буквы и цифры
def validate_login(value):
    if not re.match("^[A-Za-z0-9]+$", value):
        raise validate.ValidationError("Login must contain only letters and numbers.")

# Схема для логина
class LoginSchema(Schema):
    login = fields.Str(required=True, validate=[validate_login])
    password = fields.Str(required=True, validate=validate.Length(min=8))

# Схема для регистрации (наследует LoginSchema)
class RegisterSchema(LoginSchema):
    full_name = fields.Str(required=True)
    gender = fields.Str(required=True, validate=validate.OneOf(['male', 'female', 'other']))
    birth_date = fields.Date(required=True)
