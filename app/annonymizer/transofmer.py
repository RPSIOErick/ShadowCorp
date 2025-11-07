import hashlib
from typing import Dict




def _hash(value: str) -> str:
return hashlib.sha256(value.encode('utf-8')).hexdigest()[:8]




def anonymize(record: Dict, detected: Dict) -> Dict:
# paciente_id: hash anon
raw_id = record.get('cpf') or record.get('nome') or 'unknown'
paciente_id = f"anon_{_hash(raw_id)}"


idade = record.get('idade')
if isinstance(idade, int):
faixa = f"{(idade//10)*10}-{(idade//10)*10 + 9}"
else:
faixa = 'desconhecida'


# diagnostico: simplificado (categorização stub)
diag = record.get('diagnostico') or ''
if 'hipertens' in diag.lower():
diag_cat = 'Doença cardiovascular'
else:
diag_cat = 'Outros'


historico = record.get('historico') or []
# simplificação de histórico: remover detalhes PII
hist = [h.replace('Gripe','Infecção leve') for h in historico]


return {
'paciente_id': paciente_id,
'faixa_etaria': faixa,
'diagnostico_categoria': diag_cat,
'historico': hist,
'regiao': 'Zona Urbana - Sul'
}