from fastapi import Depends, status, APIRouter, HTTPException
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.crud import UsersRepository
from src.infra.sqlalchemy.config.database import session
from src.infra.provedores.provedor_hash import gera_hash, verefica_hash
from src.infra.provedores.provedor_token import criar_token_de_acesso
from .usuario_logado import obter_usuario_logado


rota = APIRouter()


@rota.get('/listar-usuarios')  # response_model=List[schemas.User]
def lister_users(session: Session = Depends(session)):
    users = UsersRepository(session).lister()
    return users


@rota.post('/singup', status_code=status.HTTP_201_CREATED)
def cadastra_usuario(user: schemas.User, session: Session = Depends(session)):
    """
        Rota para cadastrar usuario
    """
    user.password = gera_hash(user.password)
    user_db = UsersRepository(session).create_user(user)
    return user_db


@rota.post('/login-token', response_model=schemas.LoginSucesso)
def login(login_dados: schemas.Login, session: Session = Depends(session)):
    '''
        Rota para fazer login e ganhar um token.
    '''
    email = login_dados.email
    senha = login_dados.password

    usuario = UsersRepository(session).verefica_existencia_do_email(email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Email ou senha não existem ou incorretos')

    senha_valida = verefica_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Email ou senha não existem ou incorretos')

    # informacao usada para gera o token
    token = criar_token_de_acesso({'sub': usuario.email})

    return schemas.LoginSucesso(name=usuario.name, email=usuario.email, access_token=token)


@rota.get('/me', response_model=schemas.UserInfo)
def me(usuario: schemas.User = Depends(obter_usuario_logado)):
    return usuario

# Middleware : intercepatçao de requisicao e resposta. Sempre no meio do caminho.