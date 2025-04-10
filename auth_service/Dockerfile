# auth_service/Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

# Устанавливаем зависимости и bash (для совместимости)
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Гарантируем, что файл исполняемый
RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8003

# Указываем полный путь для надёжности
ENTRYPOINT ["/app/docker-entrypoint.sh"]