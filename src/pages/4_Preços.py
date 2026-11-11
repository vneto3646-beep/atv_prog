import streamlit as st

from src.crud import criar_preco, excluir_preco, listar_alimentos, listar_precos, atualizar_preco

st.title("💰 Preços de venda")

alimentos = listar_alimentos()
if alimentos:
    st.subheader("Cadastrar novo preço")
    with st.form("form_novo_preco"):
        alimento = st.selectbox(
            "Alimento",
            options=alimentos,
            format_func=lambda item: f"{item.id} - {item.nome}",
        )
        preco = st.number_input("Preço unitário", min_value=0.0, step=0.5, format="%.2f")
        validade = st.text_input("Validade", value="Semana atual")
        observacao = st.text_area("Observação")
        enviado = st.form_submit_button("Salvar preço")

    if enviado:
        criar_preco(alimento.id, preco, validade, observacao)
        st.success("Preço cadastrado com sucesso!")
        st.rerun()

    precos = listar_precos()
    if precos:
        st.subheader("Atualizar ou excluir preço")
        item = st.selectbox(
            "Selecione o registro de preço",
            options=precos,
            format_func=lambda registro: f"{registro.id} - {registro.alimento.nome} - R$ {registro.preco:.2f}",
        )

        with st.form("form_editar_preco"):
            alimento_edit = st.selectbox(
                "Alimento",
                options=alimentos,
                index=next((i for i, alimento_reg in enumerate(alimentos) if alimento_reg.id == item.alimento_id), 0),
                format_func=lambda item_reg: f"{item_reg.id} - {item_reg.nome}",
            )
            preco_edit = st.number_input("Preço unitário", min_value=0.0, step=0.5, value=item.preco, format="%.2f")
            validade_edit = st.text_input("Validade", value=item.validade)
            observacao_edit = st.text_area("Observação", value=item.observacao or "")

            col1, col2 = st.columns(2)
            with col1:
                atualizar = st.form_submit_button("Atualizar preço")
            with col2:
                excluir = st.form_submit_button("Excluir preço")

        if atualizar:
            atualizar_preco(item.id, alimento_edit.id, preco_edit, validade_edit, observacao_edit)
            st.success("Preço atualizado com sucesso!")
            st.rerun()

        if excluir:
            excluir_preco(item.id)
            st.success("Preço removido com sucesso!")
            st.rerun()

    tabela = [{
        "ID": item.id,
        "Alimento": item.alimento.nome,
        "Preço": f"R$ {item.preco:.2f}",
        "Validade": item.validade,
        "Observação": item.observacao or "-",
    } for item in precos]
    st.dataframe(tabela, use_container_width=True)
else:
    st.warning("Cadastre primeiro pelo menos um alimento para definir os preços.")
