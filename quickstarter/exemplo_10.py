import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

class ClienteSchema(pa.DataFrameModel):
    nome: str
    região: str
    is_cliente: bool

    class Config:
        strict = True  # Garante que nenhuma coluna extra seja permitida
        
@pa.check_types
def atualiza_cliente(dataframe: DataFrame[ClienteSchema]) -> DataFrame[ClienteSchema]:
    dataframe["is_cliente"] = True
    return ClienteSchema.validate(dataframe, lazy=True)

if __name__ == "__main__":
    # Criando um DataFrame de exemplo
    dados = {
        "nome": ["Pedro", "Ana"],
        "região": ["São Paulo", "Rio de Janeiro"],
        "is_cliente": [False, True]
    }
    df_clientes = pd.DataFrame(dados)
    
    # Validando o DataFrame contra o esquema definido
    df_validado = ClienteSchema.validate(df_clientes)
    print(df_validado)
    
    # Atualizando o status de cliente no DataFrame
    df_atualizado = atualiza_cliente(df_validado)
    # ClienteSchema.validate(df_atualizado)
    print(df_atualizado)
