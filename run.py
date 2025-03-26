from app import create_app

# Создаём экземпляр Flask-приложения из фабрики
app = create_app()

# Запускаем приложение в режиме отладки
if __name__ == "__main__":
    app.run(debug=True)
