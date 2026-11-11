import streamlit as st

from src.crud import (
    criar_alimento,
    excluir_alimento,
    listar_alimentos,
    atualizar_alimento,
)

st.title("🍔 Alimentos")

st.subheader("Cadastrar novo alimento")
with st.form("form_novo_alimento"):
    nome = st.text_input("Nome")
    categoria = st.text_input("Categoria", value="Comida")
    descricao = st.text_area("Descrição")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)
    unidade = st.text_input("Unidade", value="un")
    enviado = st.form_submit_button("Salvar alimento")

if enviado:
    criar_alimento(nome, categoria, descricao, quantidade, unidade)
    st.success("Alimento cadastrado com sucesso!")
    st.rerun()

alimentos = listar_alimentos()
if alimentos:
    st.subheader("Atualizar ou excluir alimento")
    item = st.selectbox(
        "Selecione o alimento",
        options=alimentos,
        format_func=lambda registro: f"{registro.id} - {registro.nome}",
    )

    with st.form("form_editar_alimento"):
        nome_edit = st.text_input("Nome", value=item.nome)
        categoria_edit = st.text_input("Categoria", value=item.categoria)
        descricao_edit = st.text_area("Descrição", value=item.descricao or "")
        quantidade_edit = st.number_input("Quantidade", min_value=0, step=1, value=item.quantidade)
        unidade_edit = st.text_input("Unidade", value=item.unidade)

        col1, col2 = st.columns(2)
        with col1:
            atualizar = st.form_submit_button("Atualizar alimento")
        with col2:
            excluir = st.form_submit_button("Excluir alimento")

    if atualizar:
        atualizar_alimento(item.id, nome_edit, categoria_edit, descricao_edit, quantidade_edit, unidade_edit)
        st.success("Alimento atualizado com sucesso!")
        st.rerun()

    if excluir:
        excluir_alimento(item.id)
        st.success("Alimento removido com sucesso!")
        st.rerun()

if alimentos:
    st.subheader("Lista de alimentos")
    tabela = [{
        "ID": item.id,
        "Nome": item.nome,
        "Categoria": item.categoria,
        "Descrição": item.descricao or "-",
        "Quantidade": item.quantidade,
        "Unidade": item.unidade,
    } for item in alimentos]
    st.dataframe(tabela, use_container_width=True)
else:
    st.info("Nenhum alimento cadastrado até o momento.")
