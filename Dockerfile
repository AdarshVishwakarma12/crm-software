FROM python:3.13.2

WORKDIR /projectCRM

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Environment variables (unsafe to hardcode secrets in production)
ENV DEBUG_VALUE=True
ENV ALLOWED_HOST=localhost,127.0.0.1
# Dummy values for local testing
ENV SECRET_KEY=956df69ad3ee8074f9474d3ccde2c1eb1d64b878088f6040129ef0e3d319b04c
ENV EMAIL_HOST_USER=none@gmail.com
ENV EMAIL_HOST_PASSWORD=None

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./projectCRM .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]