import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Pluviométrie CSV", layout="centered")
st.title("🌦️ Suivi Pluviométrie - Import / Export CSV")

rolling_days = 7

CSV_URL = "https://raw.githubusercontent.com/izadro/pluvihome/main/data/pluviometrie.csv"

@st.cache_data
def load_initial_data():
    df = pd.read_csv(CSV_URL)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

if "data" not in st.session_state:
    st.session_state.data = load_initial_data().to_dict(orient="records")

# ----- Import de fichier CSV -----
st.subheader("📥 Importer un fichier CSV")
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
if uploaded_file:
    imported_df = pd.read_csv(uploaded_file)
    if "Date" in imported_df.columns and "Pluviométrie" in imported_df.columns:
        imported_df["Date"] = pd.to_datetime(imported_df["Date"])
        st.session_state.data = imported_df.to_dict(orient="records")
        st.success("Données importées avec succès.")
    else:
        st.error("Le fichier doit contenir les colonnes 'Date' et 'Pluviométrie'.")

# ----- Formulaire de saisie -----
st.subheader("✏️ Ajouter une nouvelle valeur")
with st.form("formulaire"):
    jour = st.date_input("Date", value=date.today())
    pluie = st.number_input("Pluviométrie (mm)", min_value=0.0, step=0.1)
    if st.form_submit_button("Ajouter"):
        st.session_state.data.append({"Date": str(jour), "Pluviométrie": pluie})
        st.success(f"Ajouté : {pluie} mm pour le {jour}")

# ----- Affichage et graphique -----
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    df["Moyenne "+str(rolling_days)+" jours"] = df["Pluviométrie"].rolling(rolling_days, min_periods=1).mean()

    st.subheader("📊 Données enregistrées")
    st.dataframe(df)

    st.subheader("📊 Edition directe des données")
    df = st.data_editor(df, num_rows="dynamic")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df["Date"], df["Pluviométrie"], color="skyblue", label="Pluviométrie")
    ax.plot(df["Date"], df["Moyenne "+str(rolling_days)+" jours"], color="darkblue", linewidth=2, label="Moy. glissante ("+str(rolling_days)+"j)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Pluviométrie (mm)")
    ax.set_title("Historique des pluies")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # ----- Export CSV -----
    st.subheader("📤 Exporter les données")
    csv_export = df[["Date", "Pluviométrie"]].to_csv(index=False)
    st.download_button("📄 Télécharger CSV", csv_export, file_name="pluviometrie_export.csv", mime="text/csv")
else:
    st.info("Aucune donnée disponible pour le moment.")
