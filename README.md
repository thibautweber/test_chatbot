# Projet de Chatbot avec Accès Internet & Analyse VLM

Ce projet contient la solution le test technique. Il se compose de deux parties principales :

1.  Un **Chatbot web** avec un backend en Python (Flask) et un frontend en React, capable d'accéder à Internet pour répondre aux questions.
2.  Un **script d'analyse d'image** utilisant un VLM en local.

---

## Partie 1 : Chatbot avec Accès Internet

### Prérequis

* [Python 3.9+](https://www.python.org/)
* [Node.js et npm](https://nodejs.org/en/)
* Un compte [OpenRouter](https://openrouter.ai/) pour obtenir une clé API.

### Installation et Lancement

1.  **Clonez le repository :**
    ```bash
    git clone https://github.com/thibautweber/test_chatbot.git
    cd test_chatbot
    cd partie1
    ```

2.  **Configuration du Backend :**
    * Naviguez dans le dossier backend :
        ```bash
        cd backend
        ```
    * Installez les dépendances Python :
        ```bash
        pip install -r requirements.txt
        ```
    * Créez un fichier `.env` et ajoutez-y votre clé API OpenRouter :
        ```
        OPENROUTER_API_KEY="votre_clé_api"
        ```

3.  **Configuration du Frontend :**
    * Depuis la racine du projet, allez dans le dossier frontend :
        ```bash
        cd ../frontend 
        ```
    * Installez les dépendances Node.js :
        ```bash
        npm install
        ```

4.  **Lancement de l'application :**
    * **Terminal 1 (Backend) :**
        ```bash
        # Depuis le dossier /backend
        python app.py
        ```
        Le serveur backend doit tourner sur `http://localhost:5001`.

    * **Terminal 2 (Frontend) :**
        ```bash
        # Depuis le dossier /frontend
        npm start
        ```
        L'application web s'ouvrira automatiquement sur `http://localhost:3000`.

---

## Partie 2 : Tout est dans le PDF du dossier partie2

---

## Partie 3 : Script d'Analyse d'Image (VLM)

Ce script utilise un modèle de vision pour décrire le contenu d'une image.

### Prérequis

* Python avec les bibliothèques `torch`, `transformers`, et `pillow`.

    ```bash
    pip install torch transformers pillow
    ```


### Lancement

**Exécutez le script :**
* Naviguez dans le dossier partie3 :
        ```bash
        cd partie3
        ```

* Lancez le script :
    ```bash
    python script_vlm.py
    ```
    Le script téléchargera le modèle (la première fois) puis affichera une description de l'image dans la console.