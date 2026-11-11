from src.database import get_session
from src.models import Alimento, Fornecedor, Pessoa, PrecoVenda


def listar_alimentos():
    with get_session() as session:
        return session.query(Alimento).order_by(Alimento.id).all()


def criar_alimento(nome, categoria, descricao, quantidade, unidade):
    with get_session() as session:
        novo = Alimento(
            nome=nome,
            categoria=categoria,
            descricao=descricao,
            quantidade=quantidade,
            unidade=unidade,
        )
        session.add(novo)
        session.commit()
        return novo


def atualizar_alimento(alimento_id, nome, categoria, descricao, quantidade, unidade):
    with get_session() as session:
        registro = session.query(Alimento).filter_by(id=alimento_id).first()
        if not registro:
            return None
        registro.nome = nome
        registro.categoria = categoria
        registro.descricao = descricao
        registro.quantidade = quantidade
        registro.unidade = unidade
        session.commit()
        return registro


def excluir_alimento(alimento_id):
    with get_session() as session:
        registro = session.query(Alimento).filter_by(id=alimento_id).first()
        if not registro:
            return False
        session.delete(registro)
        session.commit()
        return True


def listar_fornecedores():
    with get_session() as session:
        return session.query(Fornecedor).order_by(Fornecedor.id).all()


def criar_fornecedor(nome, tipo, contato, descricao, insumos):
    with get_session() as session:
        novo = Fornecedor(
            nome=nome,
            tipo=tipo,
            contato=contato,
            descricao=descricao,
            insumos=insumos,
        )
        session.add(novo)
        session.commit()
        return novo


def atualizar_fornecedor(fornecedor_id, nome, tipo, contato, descricao, insumos):
    with get_session() as session:
        registro = session.query(Fornecedor).filter_by(id=fornecedor_id).first()
        if not registro:
            return None
        registro.nome = nome
        registro.tipo = tipo
        registro.contato = contato
        registro.descricao = descricao
        registro.insumos = insumos
        session.commit()
        return registro


def excluir_fornecedor(fornecedor_id):
    with get_session() as session:
        registro = session.query(Fornecedor).filter_by(id=fornecedor_id).first()
        if not registro:
            return False
        session.delete(registro)
        session.commit()
        return True


def listar_pessoas():
    with get_session() as session:
        return session.query(Pessoa).order_by(Pessoa.id).all()


def criar_pessoa(nome, categoria, funcao, contato, disponibilidade):
    with get_session() as session:
        nova = Pessoa(
            nome=nome,
            categoria=categoria,
            funcao=funcao,
            contato=contato,
            disponibilidade=disponibilidade,
        )
        session.add(nova)
        session.commit()
        return nova


def atualizar_pessoa(pessoa_id, nome, categoria, funcao, contato, disponibilidade):
    with get_session() as session:
        registro = session.query(Pessoa).filter_by(id=pessoa_id).first()
        if not registro:
            return None
        registro.nome = nome
        registro.categoria = categoria
        registro.funcao = funcao
        registro.contato = contato
        registro.disponibilidade = disponibilidade
        session.commit()
        return registro


def excluir_pessoa(pessoa_id):
    with get_session() as session:
        registro = session.query(Pessoa).filter_by(id=pessoa_id).first()
        if not registro:
            return False
        session.delete(registro)
        session.commit()
        return True


def listar_precos():
    with get_session() as session:
        return session.query(PrecoVenda).order_by(PrecoVenda.id).all()


def criar_preco(alimento_id, preco, validade, observacao):
    with get_session() as session:
        novo = PrecoVenda(
            alimento_id=alimento_id,
            preco=preco,
            validade=validade,
            observacao=observacao,
        )
        session.add(novo)
        session.commit()
        return novo


def atualizar_preco(preco_id, alimento_id, preco, validade, observacao):
    with get_session() as session:
        registro = session.query(PrecoVenda).filter_by(id=preco_id).first()
        if not registro:
            return None
        registro.alimento_id = alimento_id
        registro.preco = preco
        registro.validade = validade
        registro.observacao = observacao
        session.commit()
        return registro


def excluir_preco(preco_id):
    with get_session() as session:
        registro = session.query(PrecoVenda).filter_by(id=preco_id).first()
        if not registro:
            return False
        session.delete(registro)
        session.commit()
        return True
