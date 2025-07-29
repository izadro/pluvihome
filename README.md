
# 🌦️ Pluvihome

**Pluvihome** est une application Streamlit simple et rapide pour suivre la pluviométrie quotidienne depuis une interface web.

---

## 🚀 Démo en ligne

🔗 **[Lien vers l'application en ligne (exemple)]([https://share.streamlit.io/](https://pluvihome-qbycyxwotmqdbg3holvbsd.streamlit.app/)**  
_(à personnaliser après déploiement)_

---

## 📁 Structure du projet

```text
pluvihome/
│
├── pluvio.py        ← Fichier principal de l'application
├── example.csv      ← Exemple de fichier de données
└── README.md        ← Ce fichier
```

---

## 📄 Exemple de fichier `example.csv`

```csv
Date,Pluviométrie
2024-07-20,10
2024-07-21,0
2024-07-22,5
```

Le fichier doit contenir les colonnes suivantes :

- `Date` : au format ISO (ex. `2024-07-20`)
- `Pluviométrie` : quantité de pluie en millimètres

---

## 💻 Lancer en local (facultatif)

```bash
pip install streamlit pandas matplotlib
streamlit run pluvio.py
```

---

## ☁️ Déploiement sur Streamlit Cloud

1. Fork ou clone ce dépôt
2. Va sur 👉 [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connecte ton compte GitHub
4. Clique sur **"New App"**
5. Sélectionne :
   - ton dépôt GitHub (`izadro/pluvihome`)
   - le fichier principal `pluvio.py`
6. Clique sur "Deploy" 🚀

---

## 🔗 Ressources utiles

- 📘 [Documentation Streamlit](https://docs.streamlit.io/)
- ☁️ [Streamlit Cloud](https://streamlit.io/cloud)
- 📄 [Déploiement d'une app Streamlit](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)

---

## 🧑‍💻 Auteur

David Rochelet – [@izadro](https://github.com/izadro)
