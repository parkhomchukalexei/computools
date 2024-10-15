FROM python:3.10-slim

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app/requirements.txt

COPY test_database.json test_database.json
COPY .flake8 .flake8
COPY .gitignore .gitignore
COPY .pre-commit-config.yaml .pre-commit-config.yaml
COPY pyproject pyproject


ENV SUPERBENCHMARK_DEBUG=True
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
