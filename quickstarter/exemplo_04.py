def validar_nome(nome):
    """Valida se o nome é uma string não vazia."""
    return isinstance(nome, str) and nome != ""

def validar_regiao(regiao):
    """Valida se a região é uma string não vazia."""
    return isinstance(regiao, str) and regiao != ""

def validar_is_cliente(is_cliente):
    """Valida se is_cliente é um booleano."""
    return isinstance(is_cliente, bool)

def validar_estrutura(dicionario):
    """Valida a estrutura do dicionário conforme as regras estabelecidas."""
    # Verifica se todas as chaves esperadas estão presentes
    chaves_esperadas = {"nome", "região", "is_cliente"}
    if not chaves_esperadas.issubset(dicionario.keys()):
        return False, "O dicionário não contém todas as chaves esperadas."
    
    # Validações específicas para cada campo
    if not validar_nome(dicionario.get("nome", "")):
        return False, "O campo 'nome' é inválido."
    
    if not validar_regiao(dicionario.get("região", "")):
        return False, "O campo 'região' é inválido."
    
    if not validar_is_cliente(dicionario.get("is_cliente", None)):
        return False, "O campo 'is_cliente' é inválido."
    
    return True, "Validação bem-sucedida."

def atualiza_cliente(values):
    values = values.copy()
    values["is_client"] = True
    return values

# Exemplo de uso
rafael = {
    "name": "rafael",
    "region": "São Paulo",
    "is_cliente": False
}

# Vou sobrescrever rafael com o novo valor
rafael = atualiza_cliente(rafael)

# Validando a estrutura
valido, mensagem = validar_estrutura(rafael)
if valido:
    print("Dicionário válido:", mensagem)
else:
    print("Dicionário inválido:", mensagem)

print(rafael)
