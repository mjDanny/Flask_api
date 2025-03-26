from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class UserService:
    @staticmethod
    def register_user(data):
        """
        Регистрирует нового пользователя.
        - Хеширует пароль
        - Преобразует дату рождения
        - Сохраняет пользователя в базу
        """
        hashed_pw = generate_password_hash(data['password'])
        birth_date_str = data.get("birth_date")
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date() if birth_date_str else None

        user = User(
            login=data['login'],
            password=hashed_pw,
            full_name=data.get('full_name'),
            gender=data.get('gender'),
            birth_date=birth_date
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(login, password):
        """
        Проверяет логин и пароль пользователя.
        Возвращает пользователя, если аутентификация успешна.
        """
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def get_all_users(full=False):
        """
        Получает список всех пользователей.
        Если full=True, возвращает все поля.
        Иначе — только логины.
        """
        users = User.query.all()
        return [
            {
                "login": u.login,
                "full_name": u.full_name if full else None,
                "gender": u.gender if full else None,
                "birth_date": u.birth_date.strftime("%Y-%m-%d") if full and u.birth_date else None
            } for u in users
        ]
