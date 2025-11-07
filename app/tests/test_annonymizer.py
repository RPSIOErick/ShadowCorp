from app.anonymizer import detector, transformer




def test_detect_cpf():
rec = {'cpf': '123.456.789-10'}
d = detector.detect_pii(rec)
assert 'cpf' in d['cpf']




def test_transformer():
rec = {'nome': 'Maria da Silva', 'cpf': '123.456.789-10', 'idade': 45, 'diagnostico': 'Hipertensão arterial', 'historico': ['2018: Gripe']}
det = detector.detect_pii(rec)
anon = transformer.anonymize(rec, det)
assert 'paciente_id' in anon
assert anon['faixa_etaria'] == '40-49'