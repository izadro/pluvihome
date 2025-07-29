# Création d'un exemple complet de code Streamlit pour l'application de saisie de pluviométrie

streamlit_code = '''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Suivi Pluviométrie", layout="centered")

st.title("🌧️ Suivi quotidien de la pluviométrie")

# Initialisation du stockage dans la session
if "data" not in st.session_state:
    st.session_state.data = []

# Formulaire de saisie
with st.form("saisie_form"):
    col1, col2 = st.columns(2)
    with col1:
        saisie_date = st.date_input("Date", value=date.today())
    with col2:
        saisie_valeur = st.number_input("Pluviométrie (mm)", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("💾 Enregistrer")
    if submitted:
        st.session_state.data.append({"Date": saisie_date, "Pluviométrie": saisie_valeur})
        st.success(f"Valeur de {saisie_valeur} mm enregistrée pour le {saisie_date}")

# Création du DataFrame
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    df = df.sort_values("Date")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Moyenne glissante (3j)"] = df["Pluviométrie"].rolling(window=3, min_periods=1).mean()

    st.subheader("📊 Données enregistrées")
    st.dataframe(df.style.format({"Pluviométrie": "{:.1f}", "Moyenne glissante (3j)": "{:.1f}"}), use_container_width=True)

    st.subheader("📈 Graphique de la pluviométrie")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df["Date"], df["Pluviométrie"], label="Pluviométrie (mm)", color="skyblue")
    ax.plot(df["Date"], df["Moyenne glissante (3j)"], label="Moy. glissante (3j)", color="darkblue", linewidth=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Pluviométrie (mm)")
    ax.set_title("Pluviométrie quotidienne avec moyenne glissante")
    ax.grid(True)
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("Ajoute des valeurs de pluie pour voir le graphique.")
'''

# Sauvegarde du code dans un fichier .py
streamlit_path = "/mnt/data/app_pluviometrie_streamlit.py"
with open(streamlit_path, "w") as f:
    f.write(streamlit_code)

streamlit_path
