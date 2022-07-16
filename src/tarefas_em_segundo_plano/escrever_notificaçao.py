

def escrever_notificacao(email: str, mensagem:str): 
    with open('./info.txt', mode='a') as log:
        info = f'Notificacao para {email} → mensagem: {mensagem}\n'
        log.write(info)


