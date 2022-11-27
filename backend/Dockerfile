FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app/tornado-backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 81

CMD ["python", "tornado_back.py"]
