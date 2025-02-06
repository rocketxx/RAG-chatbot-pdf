# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Installazione di curl e altre dipendenze di sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copia i file di requirements e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installa Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Copia il resto del codice
COPY . .

# Esponi la porta su cui girerà Streamlit
EXPOSE 8501

# Comando per avviare Ollama e l'applicazione
CMD ollama serve & streamlit run app.py