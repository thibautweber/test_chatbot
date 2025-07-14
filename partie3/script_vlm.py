# Fichier : vlm_analyzer.py (Corrigé)
# Dépendances : pip install torch transformers pillow
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

def analyze_image_with_vlm(image_path: str, prompt: str):
    """
    Charge un VLM local (moondream2), analyse une image et répond à un prompt.
    """
    try:
       
        if torch.cuda.is_available():
            device = "cuda"
            print("CUDA is available. Using GPU.")
        elif torch.backends.mps.is_available():
            device = "mps"
            print("Apple Silicon MPS is available. Using GPU.")
        else:
            device = "cpu"
            print("No GPU detected. Using CPU.")

        model_id = "vikhyatk/moondream2"
        
        print("Chargement du modèle...")
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        print(f"Analyse de l'image : {image_path}")
        image = Image.open(image_path)
        
        enc_image = model.encode_image(image)
        
        result = model.answer_question(
            enc_image, 
            prompt, 
            tokenizer,
            max_new_tokens=512 
        )
        
        print("\n--- RÉSULTAT DU VLM ---")
        print(result)
        print("-----------------------\n")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{image_path}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == '__main__':
    analyze_image_with_vlm(
        image_path='test_image.png',
        prompt='Décris ce que tu vois dans cette image.'
    )