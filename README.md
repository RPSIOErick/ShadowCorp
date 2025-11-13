# ShadowCorp

# Projeto AI + DevOps — Anonimização de Dados Hospitalares

Privacidade e Segurança de Pacientes com Inteligência Artificial e DevOps

## 📋 Descrição do Projeto

O Projeto AI + DevOps: Anonimização de Dados Hospitalares tem como objetivo proteger a privacidade de pacientes em ambientes de saúde, garantindo que dados sensíveis não possam ser utilizados para identificar indivíduos específicos, mesmo após análises estatísticas ou consultas complexas.

A solução utiliza Inteligência Artificial (IA), Machine Learning (ML) e práticas de DevOps para construir um pipeline seguro e automatizado de anonimização de dados, prevenindo o uso indevido dessas informações por empresas externas, como corretoras de seguro, que poderiam explorar dados pessoais para encarecer seguros de vida.

## 🎯 Objetivos Principais

* Anonimizar dados sensíveis (como CPF, nome, endereço, diagnósticos e histórico clínico);
* Utilizar IA/ML real para detecção e mascaramento automático de informações pessoais;
* Aplicar técnicas estatísticas, média ponderada e privacidade diferencial (DP) para evitar reidentificação;
* Integrar o processo a pipelines DevOps (CI/CD), garantindo privacidade desde o desenvolvimento até a produção;
* Oferecer uma API segura para consulta de dados agregados e anonimizados;
* Assegurar conformidade com legislações de proteção de dados, como LGPD e GDPR.

## 🏗️ Estrutura do Projeto

```
shadowcorp/
├── app/
│   ├── main.py                  # Ponto de entrada da API
│   ├── api/
│   │   └── v1/
│   │       ├── routes.py        # Rotas da API
│   │       └── schemas.py       # Modelos Pydantic
│   ├── anonymizer/
│   │   ├── detector.py          # Detecção de PII
│   │   ├── transformer.py       # Anonimização com ML
│   │   ├── dp.py                # Ruído diferencial (DP)
│   │   └── train_model.py       # Treinamento do modelo ML
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── models.py
│   └── tests/
│       └── test_anonymizer.py
├── example_data/
│   └── sample_input.json
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── ci-cd.yml
```

## 🧩 Tecnologias Utilizadas

* Linguagem Principal: Python 3.x
* Framework de ML: Scikit-Learn (Regressão Logística)
* NLP / Detecção de Dados Sensíveis: spaCy, Regex
* DevOps: GitHub Actions (CI/CD)
* Banco de Dados: PostgreSQL / MongoDB (anonimizado)
* Segurança: Differential Privacy, Hashing, Tokenização
* API: FastAPI
* Monitoramento: Prometheus + Grafana

## ⚙️ Como Rodar o Projeto

1. Clone o repositório e entre na pasta raiz (`ShadowCorp`).
2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a API **a partir da raiz do projeto** usando:

```bash
python -m app.main
```

Isso garante que o Python reconheça `app` como módulo e consiga importar todos os pacotes internos.

5. Acesse a API no navegador ou via HTTP client:

```
http://127.0.0.1:8000/docs
```

para usar o Swagger UI e testar a rota `/anonimize`.

## 📡 Exemplo de Entrada e Saída

Entrada (JSON Original):

```json
{
  "nome": "João Silva",
  "idade": 40,
  "cpf": "111.333.222-66",
  "endereco": "Rua Carlos Sampaio",
  "diagnostico": "Diabetes"
}
```

Saída (JSON Anonimizado):

```json
{
  "paciente_id": "anon_5a1889e2",
  "faixa_etaria": "40-49",
  "diagnostico_categoria": "Doença metabólica",
  "modelo_usado": "Regressão Logística real + média ponderada + DP + autoaprendizado"
}
```

## 🔄 Integração com DevOps

* CI/CD: Automatização via GitHub Actions para testes e deploys.
* Verificação Automática: Scripts que bloqueiam a inserção de dados não anonimizados.
* Logs Seguros: Nenhum log contém dados identificáveis.
* Infraestrutura como Código: Terraform e Kubernetes para ambientes replicáveis e seguros.

## 📜 Conformidade Legal

* LGPD (Brasil)
* GDPR (UE)
* HIPAA (EUA) como referência

## ⚠️ Aviso Importante

Este projeto é educacional e experimental.
Não deve ser usado em produção sem auditoria legal e técnica adequada.

## 👥 Autores

* Eliel Godoy
* Erick Bastos
* Victor Roma