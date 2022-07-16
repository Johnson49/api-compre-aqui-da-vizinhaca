from passlib.context import CryptContext


hash_context = CryptContext(schemes=['bcrypt'])

def gera_hash(texto_puro):
    return hash_context.hash(texto_puro)

def verefica_hash(texto, hash):
    return hash_context.verify(texto, hash)

