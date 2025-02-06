# 📄 Chatbot PDF con LangChain, Chroma e Ollama  

Questo è un chatbot basato su **LangChain**, **ChromaDB** e **Ollama**, che permette di caricare un file **PDF**, indicizzarlo e interrogarlo con il modello **LLaMA 3.2**.  
L'app utilizza **Streamlit** per l'interfaccia utente e può essere eseguita in un ambiente **Docker** con **Docker Compose**.

## 🚀 Funzionalità  
- 📂 **Caricamento di file PDF**  
- 🔍 **Indicizzazione del contenuto con ChromaDB**  
- 💬 **Interrogazione del PDF tramite LLaMA 3.2 di Ollama**  
- 🌐 **Interfaccia utente semplice con Streamlit**  

## 🛠️ Requisiti  
Assicurati di avere installati:  
- **Python 3.9+**  
- **Docker e Docker Compose**  

## 📦 Installazione  

### 1️⃣ Clona il repository  
```sh
git clone https://github.com/tuo-utente/chatbot-pdf.git
cd chatbot-pdf
```

### 2️⃣ Installa le dipendenze  
Se vuoi eseguire l'app senza Docker:  
```sh
pip install -r requirements.txt
```

### 3️⃣ Avvia l'app con Docker Compose  
```sh
docker compose up --build
```
L'app sarà accessibile su **http://localhost:8501**.

## 📜 Dipendenze  
Il progetto utilizza le seguenti librerie:  

```txt
streamlit
langchain
langchain-community
chromadb
pypdf
sentence-transformers
```

## ⚙️ Struttura del Progetto  
```
📂 chatbot-pdf/
│-- 📄 Dockerfile
│-- 📄 docker-compose.yml
│-- 📄 requirements.txt
│-- 📄 app.py
│-- 📄 README.md
```

## 📝 Come Funziona  

1️⃣ **Caricamento del PDF**  
L'utente carica un file **PDF** tramite l'interfaccia **Streamlit**.  

2️⃣ **Indicizzazione del contenuto**  
Il documento viene suddiviso in pagine e trasformato in vettori con il modello `all-MiniLM-L6-v2`.  

3️⃣ **Interrogazione del PDF**  
L'utente inserisce una domanda e il chatbot risponde in base al contenuto del documento.  

## 🛠️ Configurazione Docker  

### 📄 `docker-compose.yml`
```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - '11434:11434'
    volumes:
      - ollama_data:/root/.ollama

  chatbot:
    build: .
    ports:
      - '8501:8501'
    volumes:
      - .:/app
    environment:
      - OLLAMA_HOST=ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:
```

### 📄 `Dockerfile`
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🏆 Contributi  
Se vuoi migliorare il progetto, sentiti libero di aprire una **pull request** o segnalare problemi nella sezione **Issues**.  

## 📜 Licenza  
Questo progetto è distribuito sotto licenza **MIT**.  

---

📌 **Creato con ❤️ da [Il Tuo Nome](https://github.com/tuo-utente)**
