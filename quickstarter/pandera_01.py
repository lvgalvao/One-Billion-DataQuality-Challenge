import pandas as pd
import pandera as pa
from pandera.typing import Series

# data para validar
df = pd.DataFrame({
    "coluna1": [1, 4, 0, 10, 9],
    "coluna2": [-1.3, -1.4, -2.9, -10.1, -20.4],
    "coluna3": ["valor_1", "valor_2", "valor_3", "valor_2", "valor_1"],
})

class Fruit(pa.DataFrameModel):
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool

    class Config:
        extra = "forbid" 

Schema.validate(df)