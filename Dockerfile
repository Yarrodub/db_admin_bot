# Отдельный "сборочный" образ
FROM python:3.12-slim-bookworm as compile-image
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install --no-cache -r /app/requirements.txt && \
    pip wheel --no-cache-dir --wheel-dir /opt/pip_wheels -r /app/requirements.txt

# Образ, который будет непосредственно превращаться в контейнер
FROM python:3.12-slim-bookworm as run-image
WORKDIR /app
COPY --from=compile-image /opt/pip_wheels /opt/pip_wheels
RUN pip install --no-cache /opt/pip_wheels/* && rm -rf /opt/pip_wheels
COPY . /app/
CMD ["python", "main.py"]
