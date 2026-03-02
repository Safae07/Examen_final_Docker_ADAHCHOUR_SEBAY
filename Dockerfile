# Dockerfile

#image python
FROM python:3.10-slim

#dossier de travail dans le conteneur
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Commande qui s'execute au démarrage du conteneur
CMD ["python", "evaluate.py"]