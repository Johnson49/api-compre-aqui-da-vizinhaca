from fastapi import Depends, status, APIRouter, HTTPException
from src.infra.sqlalchemy.config.database import session
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.crud import ProductsRepository
from src.schemas import schemas

rota = APIRouter()

@rota.get('/produtos' ) # response_model=List[schemas.Product] -  defini quais informaçoes devem ser retornadas como respostas.
def lister_products( session: Session = Depends(session)):
    products = ProductsRepository(session).lister()
    return products

@rota.get('/produtos/{id}')
def get_by_id( id:int, session: Session = Depends(session)):
    products = ProductsRepository(session).get_id(id)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto não encontrado com id: {id}')
    return products


@rota.put('/atualizar-produto/{id}')
def update(id:int, product: schemas.Product ,session: Session = Depends(session)):
    product = ProductsRepository(session).update(id, product)
    if not product:
        return"{'Aviso': 'Produto não existe' }"
    return product


@rota.post('/criar-produtos', status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.Product, session: Session = Depends(session)):
    produto_criado = ProductsRepository(session).create_product(product)
    return produto_criado

@rota.delete('/excluir-produto/{id}')
def delete_product(id: int, session: Session = Depends(session)):
    ProductsRepository(session).delete(id)
    return "{'Aviso: 'Produto excluido com sucessor.'}"

