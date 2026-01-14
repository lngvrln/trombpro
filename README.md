**Автор:** Гаврилина Алёна  
**Студентка:** 4 курс, группа 636-01, Сеченовский университет

### 1. Создание виртуального окружения
```bash
python -m venv venv
```

### 2. Активация виртуального окружения (Windows)
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install Django
```

### 4. Запуск проекта
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 5. Панель администратора
**URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
**Данные для входа:** логин и пароль, созданные через `createsuperuser`

После запуска сервера откройте в браузере:
- **Основное приложение:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Админ-панель:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
