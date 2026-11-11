import streamlit as st

from src.crud import (
    criar_fornecedor,
    excluir_fornecedor,
    listar_fornecedores,
    atualizar_fornecedor,
)

st.title("📦 Fornecedores")

st.subheader("Cadastrar novo fornecedor")
with st.form("form_novo_fornecedor"):
    nome = st.text_input("Nome")
    tipo = st.text_input("Tipo", value="Doação")
    contato = st.text_input("Contato")
    descricao = st.text_area("Descrição")
    insumos = st.text_input("Insumos doados")
    enviado = st.form_submit_button("Salvar fornecedor")

if enviado:
    criar_fornecedor(nome, tipo, contato, descricao, insumos)
    st.success("Fornecedor cadastrado com sucesso!")
    st.rerun()

fornecedores = listar_fornecedores()
if fornecedores:
    st.subheader("Atualizar ou excluir fornecedor")
    item = st.selectbox(
        "Selecione o fornecedor",
        options=fornecedores,
        format_func=lambda registro: f"{registro.id} - {registro.nome}",
    )

    with st.form("form_editar_fornecedor"):
        nome_edit = st.text_input("Nome", value=item.nome)
        tipo_edit = st.text_input("Tipo", value=item.tipo)
        contato_edit = st.text_input("Contato", value=item.contato or "")
        descricao_edit = st.text_area("Descrição", value=item.descricao or "")
        insumos_edit = st.text_input("Insumos doados", value=item.insumos or "")

        col1, col2 = st.columns(2)
        with col1:
            atualizar = st.form_submit_button("Atualizar fornecedor")
        with col2:
            excluir = st.form_submit_button("Excluir fornecedor")

    if atualizar:
        atualizar_fornecedor(item.id, nome_edit, tipo_edit, contato_edit, descricao_edit, insumos_edit)
        st.success("Fornecedor atualizado com sucesso!")
        st.rerun()

    if excluir:
        excluir_fornecedor(item.id)
        st.success("Fornecedor removido com sucesso!")
        st.rerun()

if fornecedores:
    st.subheader("Lista de fornecedores")
    tabela = [{
        "ID": item.id,
        "Nome": item.nome,
        "Tipo": item.tipo,
        "Contato": item.contato or "-",
        "Insumos": item.insumos or "-",
    } for item in fornecedores]
    st.dataframe(tabela, use_container_width=True)
else:
    st.info("Nenhum fornecedor cadastrado até o momento.")
