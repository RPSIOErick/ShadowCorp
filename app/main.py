from fastapi import FastAPI
from app.api.v1.routes import router as api_router
import uvicorn

app = FastAPI(title="ShadowCorp Anonymizer API")

app.include_router(api_router, prefix="/api/v1")

# Executa o servidor quando o arquivo for rodado diretamente
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
