from fastapi import APIRouter
from pydantic import BaseModel
from app.anonymizer.transformer import anonymize
from app.anonymizer.detector import detect_pii


router = APIRouter()

class Paciente(BaseModel):
    nome: str | None = None
    idade: int | None = None
    cpf: str | None = None
    endereco: str | None = None
    diagnostico: str | None = None


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/anonimize")
def anonimize_data(paciente: Paciente):
    """Aplica anonimização com média ponderada e ruído diferencial."""
    data = paciente.dict()
    detected = detect_pii(data)
    resultado = anonymize(data, detected)
    return resultado
