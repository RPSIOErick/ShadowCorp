from fastapi import APIRouter
from pydantic import BaseModel
from app.anonymizer import detector, transformer


router = APIRouter()


class InputRecord(BaseModel):
nome: str | None
cpf: str | None
endereco: str | None
idade: int | None
diagnostico: str | None
historico: list[str] | None


@router.post("/anonymize")
async def anonymize(record: InputRecord):
detected = detector.detect_pii(record.dict())
anonymized = transformer.anonymize(record.dict(), detected)
return anonymized