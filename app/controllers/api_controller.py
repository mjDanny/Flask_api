from flask import Blueprint, request, session, jsonify
from app.services.user_service import UserService
from app.schemas.user_schema import LoginSchema, RegisterSchema
from app import csrf

# Создание blueprint для API
api = Blueprint('api', __name__, url_prefix='/api')

# GET /api/get_users — список пользователей
@api.route('/get_users', methods=['GET'])
def get_users():
    # Проверка, залогинен ли пользователь
    is_logged_in = session.get('user_id') is not None
    users = UserService.get_all_users(full=is_logged_in)
    return jsonify(users), 200

# POST /api/login_user — вход в систему
@api.route('/login_user', methods=['POST'])
@csrf.exempt  # отключаем CSRF только здесь (если не используешь frontend)
def login_user():
    data = request.get_json()

    # Валидация входных данных
    errors = LoginSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    # Аутентификация пользователя
    user = UserService.authenticate_user(data['login'], data['password'])
    if not user:
        return jsonify({'message': 'Invalid login or password'}), 401

    # Сохраняем сессию (id пользователя)
    session['user_id'] = user.id
    return jsonify({'message': 'Login successful'}), 200

# POST /api/register_user — регистрация
@api.route('/register_user', methods=['POST'])
@csrf.exempt
def register_user():
    data = request.get_json()

    # Валидация данных
    errors = RegisterSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    # Создание пользователя
    user = UserService.register_user(data)
    return jsonify({'message': 'User registered'}), 201
