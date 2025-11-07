import re
from typing import Dict, List


CPF_RE = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")




def detect_pii(record: Dict) -> Dict[str, List[str]]:
"""Retorna um dicionário com campos sensíveis detectados."""
findings = {}
for k, v in record.items():
if v is None:
continue
s = str(v)
fields = []
if CPF_RE.search(s):
fields.append('cpf')
# heurística: nome se tiver espaço e letras
if k == 'nome' and len(s.split()) >= 2:
fields.append('nome')
# endereço heurístico
if k == 'endereco' and any(ch.isdigit() for ch in s):
fields.append('endereco')
findings[k] = fields
return findings