import dataclasses

def atualiza_cliente(values):
    values = values.copy()
    values["is_client"] = True
    return values

@dataclasses.dataclass
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool
    

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