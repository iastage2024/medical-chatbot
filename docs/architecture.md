
# 🏗️ Architecture du projet

Cette page décrit l’architecture technique du **Medical Chatbot**, pensée pour être :
- modulaire
- maintenable
- prête pour le cloud

---

## 📁 Structure du projet


medical-chatbot/
│
├── app/
│   ├── app.py          # API Flask
│   ├── chatbot.py      # Logique OpenAI
│   ├── safety.py       # Disclaimer médical
│   ├── prompts.json    # Prompts système
│
├── templates/          # HTML (Jinja2)
├── static/             # CSS
├── docs/               # Documentation MkDocs
├── .env                # Variables sensibles
├── requirements.txt
└── mkdocs.yml