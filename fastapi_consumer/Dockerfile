FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app/fastapi

COPY requirements_fast_api.txt .

RUN pip install -r requirements_fast_api.txt

COPY . .

EXPOSE 9999

#CMD ["uvicorn", "api_fast:foo_app", "--port", "9999", "--reload"]
