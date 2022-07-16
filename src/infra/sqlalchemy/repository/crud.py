from sqlalchemy import select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

# resposavel por criar, ler, atuazalizar e deletar qualquer informação do banco de dados.

# Atraves do corpo da requisicao, as informaçoes seram trasformadas em um modelo sql para serem adicionadas nas tabelas.


class ProductsRepository():

    def __init__(self, session: Session) -> None:
        self.session = session

    # schemas é o json, que vem no corpo da requisicao. Já o models é a estrutura que ira cria o banco de dados.
    def create_product(self, product: schemas.Product) -> models.Product:
        db_product = models.Product(
            name=product.name,
            detail=product.detail,
            price=product.price,
            available=product.available,
            user_id=product.user_id
        )
        # ira adicionar o produto no banco de dados.
        self.session.add(db_product)
        self.session.commit()  # confimando a operaçao.
        # atualizar as informaçoes do banco de dados.
        self.session.refresh(db_product)
        return db_product

    def lister(self) -> models.Product:
        # products = self.session.query(models.Product).all() # No repositorio, lidamos unicamente com modelos sql.
        stmt = select(models.Product)
        products = self.session.execute(stmt).scalars().all()
        return products

    def update(self, id: int, product: schemas.Product) -> models.Product:  # product: schemas.poduct
        update_stmt = update(models.Product).where(models.Product.id == id).values(name=product.name,
                                                                                   detail=product.detail,
                                                                                   price=product.price,
                                                                                   available=product.available,
                                                                                   user_id=product.user_id)

        self.session.execute(update_stmt)
        self.session.commit()
        return update_stmt

    def delete(self, id: int) -> None:
        self.session.query(models.Product).filter_by(id=id).delete()
        self.session.commit()

    def get_id(self, id: int) -> models.Product:
        product = self.session.query(models.Product).filter_by(id=id).first()
        return product


class UsersRepository():

    def __init__(self, session: Session) -> None:
        self.session = session

    def create_user(self, user: schemas.User) -> models.User:
        db_user = models.User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            senha=user.password,
        )

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def lister(self) -> models.User:
        stmt = select(models.User)
        users = self.session.execute(stmt).scalars().all()
        return users

    def verefica_existencia_do_email(self, email) -> models.User:
        usuario = self.session.query(
            models.User).filter_by(email=email).first()
        return usuario

    def update(self):
        ...

    def delete(self):
        ...


class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session

    def cria_pedido(self, pedido: schemas.Request,) -> models.Pedido:
        pedido = models.Pedido(
            user_id=pedido.user_id,
            produto_id=pedido.produto_id,
            quantidade=pedido.quantidade,
            local_entrega=pedido.endereco,
            tipo_entrega=pedido.tipo_entrega,
            observacao=pedido.observacao,
        )
        self.session.add(pedido)
        self.session.commit()
        self.session.refresh(pedido)
        return pedido

    def listar_pedidos(self) -> models.Pedido:
        pedido = self.session.query(models.Pedido).all()
        return pedido

    def pedido_by_id(self, id: int) -> models.Pedido:
        pedido = self.session.query(models.Pedido).filter_by(id=id).first()
        return pedido

    def atuazalizar_pedido(self):
        ...

    def cancelar_pedido(self):
        ...
