# app/anonymizer/train_model.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Exemplos simulados de diagnósticos e suas categorias
diagnosticos = [
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

categorias = [
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

# Cria um pipeline: texto → TF-IDF → Regressão Logística
modelo = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Treina o modelo
modelo.fit(diagnosticos, categorias)

# Salva o modelo treinado
joblib.dump(modelo, "app/anonymizer/modelo_diagnostico.joblib")

print("Modelo treinado e salvo com sucesso!")
