from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
#Config DO TOKEN

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITMO = os.getenv('ALGORITMO')
TEMPO_PARA_EXPIRAR_TOKEN = os.getenv('TEMPO_PARA_EXPIRAR_TOKEN ') #MINUTOS


def criar_token_de_acesso(dados: dict):
    dados_token = dados.copy()
            #       pega o agora - faz uma opreçao no tempo
    expiracao = datetime.utcnow() + timedelta(minutes=TEMPO_PARA_EXPIRAR_TOKEN)
    #atualizamos a chave 'exp' com o tempo que vai levar para expira nosso token
    dados_token.update({'exp': expiracao})
    #cria o token
    token_jwt = jwt.encode(dados_token, SECRET_KEY, algorithm=ALGORITMO)
    
    return token_jwt

def vereficar_token_de_acesso(token: str):
    # na essensia estamos encripitado o email, trasformado em um token e da mesma forma, decripitamos para fazer a validaçao.
    carga_de_dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
    #sendo assim, estou tirado da 'carga_de_dados' o email.
    return carga_de_dados.get('sub')
