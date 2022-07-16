from fastapi import Request
import time

#erro de importe. 

# Middleware : intercepatçao de requisicao e resposta. Sempre no meio do caminho.


# @app.middleware('http') 
# async def middleware_processar_tempo(request: Request, next): # marca o tempo da requisao ate a resposta da mesma.
#     print('interceptou a requisicao')
#     response = await next(request) # manda para frente a requesicao - autoriza a posseguir.
#     print('Interceptou a resposta')

#     return response