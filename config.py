import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    # Секретный ключ используется для защиты cookies, сессий, CSRF и т.п.
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_fallback_key')

    # URI для подключения к базе данных (SQLite в данном случае)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///users.db')

    # Отключение лишних уведомлений о модификациях SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Тип хранения сессии — в файловой системе
    SESSION_TYPE = 'filesystem'

    # Включение CSRF-защиты
    WTF_CSRF_ENABLED = True
