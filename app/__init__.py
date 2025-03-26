from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

# Инициализация расширений Flask (без привязки к приложению пока)
db = SQLAlchemy()
csrf = CSRFProtect()

# Фабрика приложения
def create_app():
    app = Flask(__name__)

    # Загружаем настройки из config.py
    app.config.from_object('config.Config')

    # Привязка расширений к приложению
    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)
    Session(app)

    # Регистрация API-контроллера (роутов)
    from app.controllers.api_controller import api
    app.register_blueprint(api)

    return app
