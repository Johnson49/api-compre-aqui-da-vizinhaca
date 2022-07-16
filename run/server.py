from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import user, product, pedidos
from src.tarefas_em_segundo_plano.escrever_notificaçao import escrever_notificacao




app = FastAPI()

# ----------------------------------------------------------------------
# CORS
# defini quais origens pode se comunicar com a API.
origens = ['http://127.0.0.1:8000', 'http://127.0.0.1:80', 'https://127.0.0.1']
app.add_middleware(CORSMiddleware,
                   allow_origins=origens,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

# ----------------------------------------------------------------------

# Rotas
app.include_router(product.rota, prefix='/estoque')
app.include_router(user.rota, prefix='/usuario')
app.include_router(pedidos.rota)

# -----------------------------------------------------------------------

# defini nossa tarefa que será executada em segundo plano.
@app.post('/envia-messagem/{email}')
def envia_email(email: str, mensagem: str, background: BackgroundTasks):
    # adiciona a tarefa que sera executada em segundo plano.
    background.add_task(escrever_notificacao, email,
                        mensagem)
    return {"Ok": 'Tudo certo'}


# ----------------------------------------------------------------------

# middleware
@app.middleware('http')
# marca o tempo da requisao ate a resposta da mesma.
async def middleware_processar_tempo(request: Request, next):
    print('interceptou a requisicao')
    # manda para frente a requesicao - autoriza a posseguir.
    response = await next(request)
    print('Interceptou a resposta')

    return response
