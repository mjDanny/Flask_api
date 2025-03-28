

# 🧩 Flask User API

Простой REST API на Flask для управления пользователями: регистрация, логин, вывод списка пользователей с защитой сессий и валидацией.

---

## 🚀 Возможности

- Регистрация пользователя
- Вход (с сохранением сессии)
- Получение списка пользователей
  - Если залогинен: все данные
  - Если не залогинен: только логины
- Валидация логина и пароля
- Хранение в SQLite
- CSRF защита
- Сессии через Flask Session

---

## 📦 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/yourname/flask-user-api.git
cd flask-user-api
```

2. Создай виртуальное окружение и активируй:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# или
source .venv/bin/activate      # macOS/Linux
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

4. Настрой `.env`:

Создай файл `.env` (можно из `.env.example`):

```env
SECRET_KEY=super-secret-key
DATABASE_URL=sqlite:///users.db
```

---

## 🗄 Инициализация базы данных

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

---

## ▶️ Запуск сервера

```bash
python run.py
```

После запуска:  
📍 API доступен по адресу `http://127.0.0.1:5000/api/`

---

## 🧪 Тестирование через Postman

### 🔸 Регистрация  
**POST** `/api/register_user`

```json
{
  "login": "testuser",
  "password": "securepass123",
  "full_name": "John Doe",
  "gender": "male",
  "birth_date": "1990-01-01"
}
```

---

### 🔸 Вход  
**POST** `/api/login_user`

```json
{
  "login": "testuser",
  "password": "securepass123"
}
```

---

### 🔸 Получение пользователей  
**GET** `/api/get_users`

- Если не залогинен → только логины
- Если залогинен → все данные

---

## ✅ Валидация

- Логин: только латинские буквы и цифры (`^[A-Za-z0-9]+$`)
- Пароль: минимум 8 символов
- Пол: `male`, `female`, `other`
- Дата рождения: в формате `YYYY-MM-DD`

---

## 📂 Структура проекта

```
flask_user_api/
│
├── app/
│   ├── models/           # SQLAlchemy модели
│   ├── services/         # Бизнес-логика
│   ├── controllers/      # Роуты
│   ├── schemas/          # Marshmallow схемы
│   └── utils/            # Хелперы, валидации (если нужно)
│
├── migrations/           # Flask-Migrate файлы
├── .env                  # Переменные окружения
├── config.py             # Конфигурация Flask
├── run.py                # Точка входа
├── requirements.txt      # Зависимости
└── README.md             # Документация
```

---

