from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Alimento(Base):
    __tablename__ = "alimentos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    categoria: Mapped[str] = mapped_column(String(80), default="Geral")
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    quantidade: Mapped[int] = mapped_column(Integer, default=0)
    unidade: Mapped[str] = mapped_column(String(30), default="un")
    precos: Mapped[list["PrecoVenda"]] = relationship(back_populates="alimento", cascade="all, delete-orphan")


class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    tipo: Mapped[str] = mapped_column(String(80), default="Doação")
    contato: Mapped[str | None] = mapped_column(String(150), nullable=True)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    insumos: Mapped[str | None] = mapped_column(String(200), nullable=True)


class Pessoa(Base):
    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    categoria: Mapped[str] = mapped_column(String(80), nullable=False)
    funcao: Mapped[str | None] = mapped_column(String(120), nullable=True)
    contato: Mapped[str | None] = mapped_column(String(150), nullable=True)
    disponibilidade: Mapped[str | None] = mapped_column(String(120), nullable=True)


class PrecoVenda(Base):
    __tablename__ = "precos_venda"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    alimento_id: Mapped[int] = mapped_column(ForeignKey("alimentos.id"), nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    validade: Mapped[str] = mapped_column(String(100), default="Semana atual")
    observacao: Mapped[str | None] = mapped_column(Text, nullable=True)
    alimento: Mapped["Alimento"] = relationship(back_populates="precos")
