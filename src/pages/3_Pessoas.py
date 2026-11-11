import streamlit as st

from src.crud import criar_pessoa, excluir_pessoa, listar_pessoas, atualizar_pessoa

st.title("👥 Pessoas")

st.subheader("Cadastrar nova pessoa")
with st.form("form_nova_pessoa"):
    nome = st.text_input("Nome")
    categoria = st.text_input("Categoria", value="Aluno")
    funcao = st.text_input("Função")
    contato = st.text_input("Contato")
    disponibilidade = st.text_input("Disponibilidade")
    enviado = st.form_submit_button("Salvar pessoa")

if enviado:
    criar_pessoa(nome, categoria, funcao, contato, disponibilidade)
    st.success("Pessoa cadastrada com sucesso!")
    st.rerun()

pessoas = listar_pessoas()
if pessoas:
    st.subheader("Atualizar ou excluir pessoa")
    item = st.selectbox(
        "Selecione a pessoa",
        options=pessoas,
        format_func=lambda registro: f"{registro.id} - {registro.nome}",
    )

    with st.form("form_editar_pessoa"):
        nome_edit = st.text_input("Nome", value=item.nome)
        categoria_edit = st.text_input("Categoria", value=item.categoria)
        funcao_edit = st.text_input("Função", value=item.funcao or "")
        contato_edit = st.text_input("Contato", value=item.contato or "")
        disponibilidade_edit = st.text_input("Disponibilidade", value=item.disponibilidade or "")

        col1, col2 = st.columns(2)
        with col1:
            atualizar = st.form_submit_button("Atualizar pessoa")
        with col2:
            excluir = st.form_submit_button("Excluir pessoa")

    if atualizar:
        atualizar_pessoa(item.id, nome_edit, categoria_edit, funcao_edit, contato_edit, disponibilidade_edit)
        st.success("Pessoa atualizada com sucesso!")
        st.rerun()

    if excluir:
        excluir_pessoa(item.id)
        st.success("Pessoa removida com sucesso!")
        st.rerun()

if pessoas:
    st.subheader("Lista de pessoas")
    tabela = [{
        "ID": item.id,
        "Nome": item.nome,
        "Categoria": item.categoria,
        "Função": item.funcao or "-",
        "Contato": item.contato or "-",
        "Disponibilidade": item.disponibilidade or "-",
    } for item in pessoas]
    st.dataframe(tabela, use_container_width=True)
else:
    st.info("Nenhuma pessoa cadastrada até o momento.")
