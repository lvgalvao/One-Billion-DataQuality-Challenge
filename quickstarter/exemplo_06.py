import dataclasses

@dataclasses.dataclass
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool

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
    new_rafael = Cliente(**rafael)
    print(new_rafael)

    # Atualizando o dicionário rafael
    rafael = atualiza_cliente(rafael)

    # Criando uma nova instância de Cliente com o dicionário atualizado
    rafael = Cliente(**rafael)
    print(rafael)