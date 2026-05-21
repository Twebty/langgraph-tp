# Agentic RAG Chatbot avec LangGraph

## Description du projet

Ce projet académique a pour objectif de découvrir et mettre en œuvre les concepts fondamentaux de LangGraph à travers la création d’un chatbot Agentic RAG (Retrieval-Augmented Generation).

Le projet est divisé en deux parties :

### Première Partie
Mise en œuvre des concepts de base de LangGraph en suivant la démonstration vidéo :

https://www.youtube.com/watch?v=RVUyZ9yVthk

### Deuxième Partie
Développement d’un chatbot Agentic RAG avec LangGraph en suivant la vidéo :

https://www.youtube.com/watch?v=LTVHV8JLY8E

Le projet inclut :
- Création d’un workflow multi-agents avec LangGraph
- Utilisation des modèles OpenAI via LangChain
- Génération augmentée par récupération (RAG)
- Test avec LangGraph Studio
- Développement d’une interface web avec Streamlit

---

# Technologies utilisées

- Python
- LangGraph
- LangChain
- OpenAI API
- Streamlit
- ChromaDB / Vector Store
- Retrieval-Augmented Generation (RAG)

---

# Structure du projet

```bash
LangGraph-TP/
│
├── app.py
├── streamlit_app.py
├── langgraph.json
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│
├── vectorstore/
│
└── venv/
```

---

# Fonctionnalités

## Workflow LangGraph
- Création de graphes d’agents
- Gestion des états
- Enchaînement des nœuds
- Contrôle des transitions

## Chatbot Agentic RAG
- Recherche contextuelle dans les documents
- Génération intelligente de réponses
- Mémoire conversationnelle
- Utilisation d’embeddings OpenAI

## LangGraph Studio
- Visualisation du graphe
- Test interactif des agents
- Analyse des transitions

## Interface Streamlit
- Interface utilisateur simple
- Chat interactif
- Affichage des réponses du chatbot

---

# Installation du projet

## 1. Cloner le projet

```bash
git clone https://github.com/USERNAME/LangGraph-TP.git
cd LangGraph-TP
```

---

## 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

## 3. Activer l’environnement virtuel

### Windows CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
venv\Scripts\Activate.ps1
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou :

```bash
pip install langgraph-cli[inmem] langgraph langchain-openai streamlit
```

---

# Variables d’environnement

Créer un fichier `.env` :

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_key
```

---

# Lancer LangGraph Studio

```bash
langgraph dev
```

Le serveur démarre sur :

```bash
http://127.0.0.1:2024
```

Studio :

```bash
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

---


---

# Exemple de workflow LangGraph

Le système est composé de plusieurs nœuds :

- User Input Node
- Retrieval Node
- Agent Reasoning Node
- Response Generation Node

Chaque nœud représente une étape du traitement dans le graphe.

---

# Concepts étudiés

## LangGraph
- StateGraph
- Nodes
- Edges
- Conditional Edges
- Memory
- Multi-Agent Systems

## RAG
- Embeddings
- Vector Database
- Semantic Search
- Context Retrieval

## LangChain
- Prompt Templates
- Chat Models
- Chains
- Tools

---

# Tests réalisés

- Test du workflow dans LangGraph Studio
- Test des transitions entre agents
- Validation des réponses générées
- Test de l’interface Streamlit

---

# Résultats obtenus

Le projet permet :
- la compréhension des concepts de LangGraph
- la création d’un système multi-agents
- l’intégration du RAG avec OpenAI
- l’utilisation d’une interface web interactive

---

# Auteur

Projet réalisé dans le cadre du TP LangGraph.

par :Najoua Mouaddab

# Ressources

## Vidéo 1
https://www.youtube.com/watch?v=RVUyZ9yVthk

## Vidéo 2
https://www.youtube.com/watch?v=LTVHV8JLY8E



