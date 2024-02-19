from pydantic import BaseModel, Field

class Cliente(BaseModel):
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool

    class Config:
        extra = "forbid"    

def atualiza_cliente(cliente: Cliente) -> Cliente:
    cliente.is_cliente = True
    return cliente
    
if __name__ == "__main__":

    # Nosso cliente
    rafael = {
        "nome": "pedro",
        "região": "São Paulo",
        "is_cliente": False}
    
    # Desempacotando o dicionário rafael para criar uma instância de Cliente
    cliente_rafael = Cliente(**rafael)

    print(cliente_rafael)

    # Atualizando o dicionário rafael
    cliente_rafael = atualiza_cliente(cliente_rafael)

    print(cliente_rafael)