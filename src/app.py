from pathlib import Path

import streamlit as st

from src.database import get_database_url, init_db

init_db()

BASE_DIR = Path(__file__).resolve().parent
PAGE_DIR = BASE_DIR / "pages"

st.set_page_config(
    page_title="Festa IFC",
    page_icon="🎉",
    layout="wide",
)

st.title("🎉 Sistema de Gestão da Festa do IFC Campus Blumenau")
st.caption("Organização de alimentos, fornecedores, voluntários e precificação")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧾 Visão geral")
        st.write("Este sistema ajuda a planejar a festa escolar com foco em alimentos, doações e equipe de apoio.")
    with col2:
        st.info(f"Banco ativo: {get_database_url()}")

pages = [
    st.Page(PAGE_DIR / "0_Inicio.py", title="Início", icon="🏠"),
    st.Page(PAGE_DIR / "1_Alimentos.py", title="Alimentos", icon="🍔"),
    st.Page(PAGE_DIR / "2_Fornecedores.py", title="Fornecedores", icon="📦"),
    st.Page(PAGE_DIR / "3_Pessoas.py", title="Pessoas", icon="👥"),
    st.Page(PAGE_DIR / "4_Preços.py", title="Preços", icon="💰"),
]

navigation = st.navigation(pages)
navigation.run()
