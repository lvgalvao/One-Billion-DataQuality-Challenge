import pandas as pd
import pandera as pa
from pandera.typing import Series

# data para validar
df = pd.DataFrame({
    "coluna1": [1, 4, 0, 10, 9],
    "coluna2": [-1.3, -1.4, -2.9, -10.1, "-20.4"], # <- erro
    "coluna3": ["valor_1", "valor_2", "valor_3", "valor_2", "valor_1"],
})

class Schema(pa.DataFrameModel):

    coluna1: int = pa.Field(le=10)
    coluna2: float = pa.Field(lt=-1.2)
    coluna3: str = pa.Field(str_startswith="valor_")

    @pa.check("coluna3")
    def column_3_check(cls, series: Series[str]) -> Series[bool]:
        """Verifique que a terceira coluna tenha 2 elementos após a separação do '_'"""
        return series.str.split("_", expand=True).shape[1] == 2

print(df_errado)
# Schema.validate(df_errado)