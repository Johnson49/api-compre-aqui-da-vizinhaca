import email
from itertools import product
from xml.dom.expatbuilder import InternalSubsetExtractor
from pydantic import BaseModel
from typing import Optional, List

from yaml import BaseLoader

# USado no corpo da requisação.


class User(BaseModel):
    name: str
    phone: int
    email: str
    password: str

    # my_produtcs: List[Produtc]
    # my_sales: List[Request] #minhas vendas
    # my_requests: List[Request]

    class Config:
        orm_mode = True
# -----------------------------------------------------------------------


class Login(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

# ---------------------------------------------------------------------------------------------

class LoginSucesso(BaseModel):
    name: str
    email: str
    access_token: str


# -----------------------------------------------------------------------
class UserInfo(BaseModel):
    id: int
    name: str
    email: str
    phone: int

    class Config:
        orm_mode = True

# ----------------------------------------------------------------------


class Product(BaseModel):
    # user: User
    name: str
    price: float  # preço
    detail: str  # detalhe
    available: bool  # disponivel
    user_id: int

    class Config:
        # Converte um modelo sql em um schemas (json) automaticamente.
        orm_mode = True

# -----------------------------------------------------------------------


class ProductInfo(BaseModel):
    id: int
    name: str
    detail: str
    disponivel: bool
    user_id: int
    price: float  # preço
    user: Optional[User]

    class Config:
        # Converte um modelo sql em um schemas (json) automaticamente.
        orm_mode = True

# -----------------------------------------------------------------------


class Request(BaseModel):  # pedido

    user_id: int
    produto_id: int
    quantidade: int
    tipo_entrega: str  # entrega
    endereco: Optional[str]
    observacao: Optional[str] = 'Sem observações.'  # observaçoes/comentario

    class Config:
        orm_mode = True
