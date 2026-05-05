import json
from openai import OpenAI
from app.safety import DISCLAIMER

# Le client OpenAI lit automatiquement OPENAI_API_KEY depuis .env
client = OpenAI()

def load_prompts():
    with open("app/prompts.json", encoding="utf-8") as f:
        return json.load(f)

def get_response(symptoms: str):
    prompts = load_prompts()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": prompts["system"]["content"]
            },
            {
                "role": "user",
                "content": f"Voici mes symptômes : {symptoms}"
            }
        ],
        temperature=0.3
    )

    # ✅ EXTRACTION ROBUSTE DU TEXTE (clé du bug)
    try:
        bot_text = response.output[0].content[0].text
    except Exception:
        bot_text = "Erreur : réponse OpenAI non lisible."

    return f"{DISCLAIMER}\n\n{bot_text}"