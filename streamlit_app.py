import streamlit as st
import pandas as pd

st.title("🔎 Data Analyzer - Lazarus Alphabay Edition")

# Upload CSV file
uploaded_file = st.file_uploader("Unggah file CSV kamu", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File berhasil dibaca!")

    # Tampilkan preview data
    st.subheader("👀 Pratinjau Data")
    st.dataframe(df.head())

    # Pilih kolom dari user
    st.subheader("📌 Pilih Kolom")
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    selected_column = st.selectbox("Pilih kolom numerik untuk dianalisis", numeric_columns)

    if selected_column:
        st.subheader(f"📊 Analisis Kolom: {selected_column}")
        st.write(f"Jumlah: {df[selected_column].sum():,.2f}")
        st.write(f"Rata-rata: {df[selected_column].mean():,.2f}")
        st.write(f"Maksimum: {df[selected_column].max():,.2f}")
        st.write(f"Minimum: {df[selected_column].min():,.2f}")

        # Tambahan grafik
        st.subheader("📈 Grafik Distribusi")
        st.bar_chart(df[selected_column])
