FROM python:3.10

WORKDIR /app

COPY user_module/ /app/user_module/


RUN pip install fastapi uvicorn PyYAML

EXPOSE 8000

CMD ["uvicorn", "user_module.user_api:app", "--host", "0.0.0.0", "--port", "8000"]
