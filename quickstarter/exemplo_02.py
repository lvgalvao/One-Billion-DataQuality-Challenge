
# Nossa função de atualizar cliente
def atualiza_cliente(values: dict) -> dict:
    values = values.copy()
    values["is_client"] = True
    return values

# Nosso cliente
rafael: dict = {
    "nome": "rafael",
    "região": "São Paulo",
    "is_cliente": False}

# Vou sobrescrever rafael com o novo valor
rafael = atualiza_cliente(rafael)

print(rafael)