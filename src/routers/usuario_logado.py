from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import session
from src.infra.provedores.provedor_token import vereficar_token_de_acesso
from src.infra.sqlalchemy.repository.crud import UsersRepository


# defimos o que queremos pegar.
oauth1_schema = OAuth2PasswordBearer(tokenUrl='token')

# decodificar o token, pega o email, busca no banco de dados e retornar.
def obter_usuario_logado(token: str = Depends(oauth1_schema), session: Session = Depends(session)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')

    try:
        # O token vai ser provido automaticamente
        email = vereficar_token_de_acesso(token)
    except JWTError:  # significa que naõ foi possivel decodificar o teken. Token invalido.
        raise exception # nao atualizado

    if not email:
        raise exception

    usuario = UsersRepository(session).verefica_existencia_do_email(email)

    if not usuario:  # Mais uma verificaçao para o caso de se usar um token de um usuario que nao exista mais no banco de dados.
        raise exception

    return usuario
