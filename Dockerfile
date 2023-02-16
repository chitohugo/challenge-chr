FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /challenge
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]