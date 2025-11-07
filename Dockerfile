FROM python:3.10-slim

WORKDIR /code

# Copia o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . /code

# Expõe a porta do FastAPI
EXPOSE 8000

# Executa o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
