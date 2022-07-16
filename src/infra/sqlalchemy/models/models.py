from click import password_option
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship

#Criar a estrutura das tabelas no banco de dados.

class Product(Base):
    
    __tablename__ = 'Product'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float) #preco
    available = Column(Boolean) #disponivel
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates='products')
    # pedidos = relationship('Pedido', back_populates='produto')

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    senha = Column(String)
    email = Column(String, unique=True)
    phone = Column(Integer)

    products = relationship('Product', back_populates='user') #video 25 - revisar
    pedidos = relationship('Pedido', back_populates='usuario')


class Pedido(Base):
    __tablename__ = 'Pedido'
    
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('User.id'))
    produto_id = Column(Integer, ForeignKey('Product.id'))

    usuario = relationship('User', back_populates='pedidos')


    quantidade = Column(Integer)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacao = Column(String)

