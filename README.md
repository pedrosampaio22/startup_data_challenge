# Startup_Data_Challenge

Dashboard de análise de eficiência de sustentabilidade para empresas.

## Instalação

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Para ver insights e análises do projeto
python analysis_insights.ipynb

# Para executar o dashboard.py
streamlit run dashboard.py