# setup guide
1. Створити нове віртуальне оточення + активувати його
```cmd
python -m venv %pyenv%\home_work_11
%pyenv%\home_work_11\scripts\activate.bat

2. isntall poetry
```cmd
pip install poetry
```
3. ініціалізація поетрі проекту в існуючій папці
```cmd
poetry init
```
4. install  packages
```cmd
poetry add fastapi
poetry add uvicorn[standard]
poetry add sqlalchemy
poetry add psycopg2
poetry add alembic
poetry add pydantic[email]
```
5. create & run docker container with postgres
```cmd
docker run --name postgres-goit-hw11 -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
```
6. ініціалізація створення оточення alembic
```cmd
    cd <root fodler of project>
    alembic init migrations
```
7. створеюємо міграційний скрпит для створення схеми БД
```cmd
alembic revision --autogenerate -m 'Init'
```
8. накатуємо цей міграційни скорпит в саму БД
```cmd
alembic upgrade head
```
9. run uvicorn web server
```cmd
uvicorn main:app --host localhost --port 8000 --reload
```