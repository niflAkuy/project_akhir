import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.write('# Dashboard Bike Sharing :sparkles:')

# Load Data
@st.cache_data
def load_data():
    main_df = pd.read_csv("main_data.csv")
    return main_df
df = load_data()

st.sidebar.title("Dashboard Bike Sharing")
view = st.sidebar.selectbox("Pilih Visualisasi", ["Ringkasan Data", "Penyewaan Berdasarkan Musim", "Tren Penyewaan Harian"])

# Ringkasan Data
if view == "Ringkasan Data":   
    st.write("## Data Penyewaan Sepeda")
    st.write(df.head())
    st.write("#### Statistik deskriptif berdasarkan kategori hari kerja dan jam")
    st.write(df.groupby(["workingday", "hr"])["cnt"].describe().reset_index())
    st.write("#### Pengelompokkan data berdasarkan musim (season)")
    st.write(df.groupby("season")["cnt"].describe())

# Visualisasi Penyewaan Berdasarkan Musim
elif view == "Penyewaan Berdasarkan Musim":

    st.write("### Distribusi Penyewaan Sepeda Berdasarkan Musim")
    # Boxplot Rata-rata Penyewaan Sepeda Berdasarkan Musim
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="season", y="cnt", data=df, palette="GnBu", ax=ax)
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-Rata Penyewaan Sepeda")
    st.pyplot(fig)

    # Barplot Rata-rata Penyewaan Sepeda Berdasarkan Musim
    musim = df.groupby(["season"])["cnt"].describe().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="season", y="mean", data=musim, palette="GnBu", ax=ax)
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim", fontsize=14)
    st.pyplot(fig)

elif view == "Tren Penyewaan Harian":
    st.write("### Tren Penyewaan Sepeda Berdasarkan Jam (Hari Kerja vs Hari Libur)")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", hue="workingday", data=df, marker="o")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-Rata Jumlah Penyewaan Sepeda")

    garis_tanda, labels = ax.get_legend_handles_labels()
    plt.legend(handles=garis_tanda, labels=["Hari Libur", "Hari Kerja"], title="Kategori")
    plt.xticks(range(0, 24))  # menampilkan range jam 0-23

    st.pyplot(fig)

st.sidebar.write("**Sumber Data:** Dataset Bike-sharing-dataset")


st.caption('Copyright © MC329D5Y0853')