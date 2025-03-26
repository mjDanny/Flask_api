from app import db
from datetime import datetime

# SQLAlchemy-модель для таблицы пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    login = db.Column(db.String(64), unique=True, nullable=False)  # Уникальный логин
    password = db.Column(db.String(128), nullable=False)  # Хешированный пароль
    full_name = db.Column(db.String(100))  # Полное имя пользователя
    gender = db.Column(db.String(10))  # Пол: male/female/other
    birth_date = db.Column(db.Date)  # Дата рождения
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Дата регистрации
