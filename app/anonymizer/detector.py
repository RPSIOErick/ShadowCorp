import re
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# Expressão regular para CPF
CPF_RE = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")

# Treinamento básico de detecção de PII
training_data = [
    ("João da Silva", "nome"),
    ("Rua das Flores, 123", "endereco"),
    ("123.456.789-00", "cpf"),
    ("Diagnóstico: hipertensão", "diagnostico"),
    ("Maria Oliveira", "nome"),
    ("Av. Paulista 1000", "endereco"),
]

texts = [x[0] for x in training_data]
labels = [x[1] for x in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=500)
model.fit(X, labels)


def detect_pii(record):
    """Detecta tipos de PII usando um modelo ML simples."""
    findings = {}
    for k, v in record.items():
        if v is None:
            continue

        s = str(v)

        # Prioriza regex pra CPF
        if CPF_RE.search(s):
            findings[k] = ["cpf"]
            continue

        # Usa o modelo pra prever o tipo de dado
        x = vectorizer.transform([s])
        pred = model.predict(x)[0]
        findings[k] = [pred]

    return findings
