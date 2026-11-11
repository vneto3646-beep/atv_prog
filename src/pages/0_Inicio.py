import streamlit as st

from src.crud import listar_alimentos, listar_fornecedores, listar_pessoas, listar_precos

st.title("🏠 Início")

alimentos = listar_alimentos()
fornecedores = listar_fornecedores()
pessoas = listar_pessoas()
precos = listar_precos()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Alimentos", len(alimentos))
col2.metric("Fornecedores", len(fornecedores))
col3.metric("Pessoas", len(pessoas))
col4.metric("Preços", len(precos))

st.write("### Resumo do planejamento")
st.markdown(
    """
    - Definir os alimentos a serem vendidos na festa;
    - Registrar quem vai doar os insumos;
    - Organizar as pessoas que vão atuar no evento;
    - Informar os valores de venda dos produtos;
    - Manter a festa funcional, organizada e com apoio de doações.
    """
)

with st.expander("Visualização rápida dos alimentos"):
    if alimentos:
        dados = [{
            "ID": item.id,
            "Nome": item.nome,
            "Categoria": item.categoria,
            "Quantidade": item.quantidade,
            "Unidade": item.unidade,
        } for item in alimentos]
        st.dataframe(dados, use_container_width=True)
    else:
        st.info("Ainda não há alimentos cadastrados.")
