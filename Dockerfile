FROM python:3.10

WORKDIR /app
COPY requirements.txt .
COPY . .

RUN pip install --upgrade pip \
    &&  pip install -r requirements.txt

# CMD ["uvicorn","main:app", "--reload"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]