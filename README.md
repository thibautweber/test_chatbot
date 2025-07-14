# Projet de Chatbot avec Accès Internet & Analyse VLM

Ce projet contient la solution le test technique. Il se compose de deux parties principales :

1.  Un **Chatbot web** avec un backend en Python (Flask) et un frontend en React, capable d'accéder à Internet pour répondre aux questions.
2.  Un **script d'analyse d'image** utilisant un VLM en local.

---

## 🚀 Partie 1 : Chatbot avec Accès Internet

### Prérequis

* [Python 3.9+](https://www.python.org/)
* [Node.js et npm](https://nodejs.org/en/)
* Un compte [OpenRouter](https://openrouter.ai/) pour obtenir une clé API.

### Installation et Lancement

1.  **Clonez le repository :**
    ```bash
    git clone [URL_DE_VOTRE_REPO]
    cd [NOM_DE_VOTRE_REPO]
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
        OPENROUTER_API_KEY="votre_clé_api_ici"
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

## 🖼️ Partie 2 : Script d'Analyse d'Image (VLM)

Ce script utilise un modèle de vision pour décrire le contenu d'une image.

### Prérequis

* Python avec les bibliothèques `torch`, `transformers`, et `pillow`.
    ```bash
    pip install torch transformers pillow
    ```
* (Optionnel) Un GPU avec au moins 8GB de VRAM pour des performances optimales. Le script fonctionnera sur CPU mais sera très lent.

### Lancement

1.  **Préparez votre image :**
    * Placez une image que vous souhaitez analyser à la racine du projet (ou n'importe où ailleurs) et nommez-la, par exemple, `image_a_tester.png`.

2.  **Exécutez le script :**
    * (Assurez-vous d'avoir un fichier `vlm_analyzer.py` comme celui que nous avons créé).
    * Lancez le script en lui passant le chemin de l'image :
        ```bash
        python vlm_analyzer.py --image "chemin/vers/votre/image_a_tester.png"
        ```
    Le script téléchargera le modèle (la première fois) puis affichera une description de l'image dans la console.