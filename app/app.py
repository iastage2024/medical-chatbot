import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

from app.chatbot import get_response

# Chargement des variables d'environnement
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "..", "templates"),
    static_folder=os.path.join(BASE_DIR, "..", "static")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        symptoms = data.get("symptoms")

        if not symptoms:
            return jsonify({"error": "Symptômes requis"}), 400

        response = get_response(symptoms)
        return jsonify({"response": response})

    except Exception as e:
        print("❌ ERREUR API CHAT :", e)
        return jsonify({"error": "Erreur serveur interne"}), 500

if __name__ == "__main__":
    app.run(debug=True)