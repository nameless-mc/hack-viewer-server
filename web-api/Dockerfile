FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install sqlalchemy mysqlclient
COPY . /app

CMD ["python", "-B", "src/main.py"]