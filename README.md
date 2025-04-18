# 🛡️ Access Control System (Django)

This is an educational project that simulates the operation of a bank's security system. It uses Django and PostgreSQL to emulate an access control system: you can track who is currently inside the building, how long they've been there, and view detailed information about each passcard.

## 📂 Project Structure

```bash
.
├── datacenter/                     # Django app with business logic and data views
│   ├── active_passcards_view.py   # View displaying currently active passcards
│   ├── get_visit_duration.py      # Utility for calculating visit durations
│   ├── models.py                  # Django models: Passcard and Visit
│   ├── passcard_info_view.py      # View with detailed info for a specific passcard
│   ├── storage_information_view.py# View showing who is currently inside
│   └── templates/                 # HTML templates for the web interface
│
├── main.py                        # Entry point for local debugging or testing
├── manage.py                      # Django management utility (migrate, runserver, etc.)
│
├── project/
│   ├── settings.py                # Project settings, including database config
│   └── urls.py                    # URL routes configuration
│
├── .env                           # Environment variables (DB, keys, settings)
├── requirements.txt              # Python dependencies (Django, psycopg2, etc.)
├── pyproject.toml                # Poetry configuration file
├── poetry.lock                   # Locked dependency versions
└── venv/                          # Python virtual environment
```

## ⚙️ Technologies

- Python 3.10+
- Django 3.2
- PostgreSQL
- `environs` for managing environment variables
- `psycopg2-binary` for PostgreSQL integration

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root with your settings:

```env.example
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
DEBUG=
```

5. **Start the development server:**

```bash
python manage.py runserver 0.0.0.0:8000
```

## 🖥️ Usage

After starting the server, open your browser and go to [http://0.0.0.0:8000/](http://0.0.0.0:8000/) to view:

- Who is currently inside the facility
- How long they've been inside
- A history of all visits
- Detailed info about each passcard

## 🔐 Notes

- This project uses **PostgreSQL** — make sure it’s installed and accessible.
- Secrets and credentials are stored securely in the `.env` file.
- The project is simplified for educational purposes and may omit some production-level features.

# 🛡️ Система контроля доступа (Django)

Это учебный проект, эмулирующий работу системы безопасности в банке. С помощью Django и PostgreSQL реализована имитация пропускной системы: можно отслеживать, кто находится внутри помещения, как долго длился визит, и просматривать детали по каждому пропуску.

## 📂 Структура проекта

```bash
.
├── datacenter/                     # Django-приложение с бизнес-логикой и отображением данных
│   ├── active_passcards_view.py   # Вьюшка, отображающая активные пропуски
│   ├── get_visit_duration.py      # Утилита для расчёта длительности визитов
│   ├── models.py                  # Django-модели: Passcard и Visit
│   ├── passcard_info_view.py      # Вьюшка с детальной информацией по пропускам
│   ├── storage_information_view.py# Вьюшка, отображающая людей на объекте
│   └── templates/                 # HTML-шаблоны для отображения информации
│
├── main.py                        # Точка входа при локальном запуске (например, для отладки)
├── manage.py                      # Управление Django (migrate, createsuperuser, runserver и т.д.)
│
├── project/
│   ├── settings.py                # Основные настройки проекта, включая подключение к базе данных
│   └── urls.py                    # Список маршрутов (routes/URLs)
│
├── .env                           # Переменные окружения (БД, ключи и настройки)
├── requirements.txt              # Список Python-зависимостей (Django, psycopg2 и др.)
├── pyproject.toml                # Файл конфигурации Poetry
├── poetry.lock                   # Зафиксированные версии зависимостей
└── venv/                          # Виртуальное окружение Python
```

## ⚙️ Технологии

- Python 3.10+
- Django 3.2
- PostgreSQL
- `environs` для управления переменными окружения
- `psycopg2-binary` для работы с PostgreSQL

## 📦 Установка

1. **Клонируй репозиторий:**

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. **Создай и активируй виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

3. **Установи зависимости:**

```bash
pip install -r requirements.txt
```

4. **Создай `.env` файл** в корне проекта и укажи в нём настройки:

```env.example
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
DEBUG=
```

5. **Запусти локальный сервер (для отладки):**

```bash
python manage.py runserver 0.0.0.0:8000
```

## 🖥️ Использование

После запуска ты можешь открыть браузер и перейти по адресу [http://0.0.0.0:8000/](http://0.0.0.0:8000/) для просмотра информации:

- Кто сейчас находится на объекте
- Сколько времени они уже там
- Все визиты и их длительность
- Подробности по каждому пропуску

## 🔐 Примечания

- Проект использует **PostgreSQL**, убедись, что он установлен и доступен.
- Пароли и ключи не хранятся в коде — всё подключение через `.env`.
- Проект предназначен для обучения, поэтому часть данных и логики может быть упрощена.
