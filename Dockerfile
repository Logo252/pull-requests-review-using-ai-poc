FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "main:app", "--bind", ":5000", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--reload"]