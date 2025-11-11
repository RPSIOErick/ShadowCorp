import hashlib
import joblib
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from app.anonymizer.dp import add_dp_noise

# Caminho do modelo treinado
MODEL_PATH = "app/anonymizer/modelo_diagnostico.joblib"

# Dados base iniciais
diagnosticos_base = [
    "hipertensão arterial",
    "pressão alta",
    "infarto do miocárdio",
    "asma brônquica",
    "doença pulmonar obstrutiva crônica",
    "sinusite crônica",
    "diabetes tipo 2",
    "hipoglicemia",
    "colesterol alto",
    "depressão",
    "ansiedade generalizada",
    "transtorno bipolar"
]

categorias_base = [
    "Doença cardiovascular",
    "Doença cardiovascular",
    "Doença cardiovascular",
    "Doença respiratória",
    "Doença respiratória",
    "Doença respiratória",
    "Doença metabólica",
    "Doença metabólica",
    "Doença metabólica",
    "Doença mental",
    "Doença mental",
    "Doença mental"
]


def _criar_modelo():
    """Cria e treina o modelo inicial."""
    modelo = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    modelo.fit(diagnosticos_base, categorias_base)
    joblib.dump(modelo, MODEL_PATH)
    return modelo


# Carrega ou cria o modelo
if os.path.exists(MODEL_PATH):
    modelo = joblib.load(MODEL_PATH)
else:
    modelo = _criar_modelo()


def _hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:8]


def _retrain_model(novo_diag: str, nova_categoria: str):
    """Re-treina o modelo incrementalmente com o novo diagnóstico."""
    global modelo
    try:
        # Carrega dados antigos
        X, y = diagnosticos_base.copy(), categorias_base.copy()
        # Adiciona novo exemplo
        X.append(novo_diag)
        y.append(nova_categoria)
        # Recria e treina
        modelo = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("clf", LogisticRegression(max_iter=1000))
        ])
        modelo.fit(X, y)
        joblib.dump(modelo, MODEL_PATH)
    except Exception as e:
        print(f"[ERRO] Falha ao re-treinar o modelo: {e}")


def anonymize(record, detected):
    """Aplica anonimização com Machine Learning real e re-treino automático."""
    # ID anônimo
    raw_id = record.get("cpf") or record.get("nome") or "unknown"
    paciente_id = f"anon_{_hash(raw_id)}"

    # Faixa etária com média ponderada + ruído DP
    idade = record.get("idade")
    if isinstance(idade, int):
        pesos = np.array([0.2, 0.5, 0.3])
        faixas = np.array([idade - 5, idade, idade + 5])
        faixa_media = np.average(faixas, weights=pesos)
        faixa_media_ruido = add_dp_noise(faixa_media, epsilon=0.5)
        faixa = f"{int(faixa_media_ruido//10)*10}-{int(faixa_media_ruido//10)*10 + 9}"
    else:
        faixa = "desconhecida"

    # Diagnóstico — predição ML real
    diag = record.get("diagnostico") or ""
    try:
        diag_cat = modelo.predict([diag])[0]
    except Exception:
        diag_cat = "Desconhecida"

    # ✅ Autoaprendizado — re-treina com o novo diagnóstico e categoria
    _retrain_model(diag, diag_cat)

    return {
        "paciente_id": paciente_id,
        "faixa_etaria": faixa,
        "diagnostico_categoria": diag_cat,
        "modelo_usado": "Regressão Logística real + média ponderada + DP + autoaprendizado"
    }