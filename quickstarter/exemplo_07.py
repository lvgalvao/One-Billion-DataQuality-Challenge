from pydantic.dataclasses import dataclass

@dataclass
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool

    class Config:
        extra = "forbid"    

def atualiza_cliente(cliente: Cliente) -> Cliente:
    cliente = cliente.copy()
    cliente["is_client"] = True
    return cliente
    
if __name__ == "__main__":

    # Nosso cliente
    rafael = {
        "nome": "pedro",
        "região": "São Paulo",
        "is_cliente": False}
    
    print(rafael)
    
    # Desempacotando o dicionário rafael para criar uma instância de Cliente
    rafael = Cliente(**rafael)
    print(rafael)

    # Atualizando o dicionário rafael
    rafael = atualiza_cliente(rafael)

    # Criando uma nova instância de Cliente com o dicionário atualizado
    rafael = Cliente(**rafael)
    print(rafael)