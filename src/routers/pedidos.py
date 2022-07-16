from fastapi import APIRouter, Depends,status, HTTPException
from sqlalchemy import null
from src.infra.sqlalchemy.config.database import session
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.crud import RepositorioPedido

rota = APIRouter()

@rota.get('/pedidos')
def lista_pedidos(session: Session = Depends(session)):
    pedidos = RepositorioPedido(session).listar_pedidos()
    return pedidos


@rota.get('/pedidos/{id}')
def lista_pedidos(id: int, session: Session = Depends(session)):
    pedido = RepositorioPedido(session).pedido_by_id(id)
    if not pedido: 
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Produto não encontrado com id: {id}')
    return pedido


@rota.post('/criar-pedido', status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: schemas.Request ,session: Session = Depends(session)):
    pedido = RepositorioPedido(session).cria_pedido(pedido)
    return pedido
