# 🩺 Medical Chatbot – Documentation

Bienvenue dans la documentation officielle du **Medical Chatbot**, un assistant médical éducatif développé en **Python**, **Flask** et **OpenAI**.

Ce projet a pour objectif de fournir des **informations médicales générales**, sans jamais remplacer un professionnel de santé.

---

## ⚠️ Avertissement médical

!!! warning
    Ce chatbot **ne fournit aucun diagnostic médical**.  
    Les informations sont uniquement **éducatives**.  
    En cas de symptômes graves ou persistants, consultez un médecin.

---

## ✨ Fonctionnalités principales

- API REST avec Flask
- Interface web moderne (HTML/CSS)
- Avatar médecin 🧑‍⚕️
- Animation *« le bot écrit… »*
- Loader pendant l’appel OpenAI
- Prompts externalisés en JSON
- Gestion sécurisée des clés API
- Prêt pour Docker, CI/CD et Google Cloud Run

---

## 🧱 Architecture globale

```text
Frontend (HTML/CSS)
        ↓
Flask API (REST)
        ↓
Chatbot logic
        ↓
OpenAI API