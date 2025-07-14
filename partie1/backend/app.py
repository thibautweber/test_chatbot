import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
from ddgs import DDGS

load_dotenv()

# Flask
app = Flask(__name__)
CORS(app)  # Autoriser les requêtes cross-origin pour le frontend React 


client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def perform_web_search(query: str, max_results: int = 5) -> str:
    """Effectue une recherche web avec DuckDuckGo et retourne les résultats formatés."""
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=max_results)]
            return "\n".join([f"Source: {res['href']}\nSnippet: {res['body']}" for res in results])
    except Exception as e:
        print(f"Erreur de recherche Web : {e}")
        return "La recherche web a échoué."

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint principal pour le chat."""
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Message manquant"}), 400

    try:
        # Étape 1: recherche web basée sur le message de l'utilisateur
        search_results = perform_web_search(user_message)

        # Étape 2: création du prompt pour le LLM 
        system_prompt = "Tu es un assistant IA. Réponds à la question de l'utilisateur en te basant sur les résultats de recherche web suivants. Sois concis et cite tes sources."
        
        full_prompt = f"Résultats de la recherche web:\n---\n{search_results}\n---\nQuestion de l'utilisateur: {user_message}"

        # Étape 3: appeler le LLM avec les résultats
        response = client.chat.completions.create(
            model="qwen/qwen-2.5-7b-instruct", #j'ai utilisé ce modèle car celui dans le PDF générait des erreurs
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt},
            ],
        )
        
        bot_response = response.choices[0].message.content
        return jsonify({"reply": bot_response})

    except Exception as e:
        # Gestion des erreurs (API, rate limits, etc.)
        print(f"Erreur API LLM : {e}")
        return jsonify({"error": "Désolé, une erreur est survenue lors de la communication avec le modèle de langue."}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)