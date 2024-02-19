# Contexto

Como garantir que a transformação está sendo feito da forma correta?

Temos esse excel e precisamos garantir que a transformação está sendo bem realizada 

```python
def atualiza_cliente(values):
    values = values.copy()
    values["is_client"] = True
    return values
```

Temos o dataset

```python
rafael = {
    "nome": "rafael",
    "região": "São Paulo",
    "is_cliente": False}
```

O que acontece se eu aplicar a função?

```python
atualiza_cliente(rafael)
```

Apresentar `exemplo_01`

## Abordagem Typing Dict

Esse são os nossos requisitos

Precisamos documentar uma meneira de documentar e forçar o Schema
  - Quais são o nome das colunas ?
  - Quais são os *DataType* e *Constraints* ?
  - Quais são os valores padrão dessa coluna ?
  - Quais estruturas são `nested` e ordenadas ?
  - Essa coluna permite `null` ?

Dicionários não atendem os nossos requisitos

Além disso, a longo prazo, essa
- Baixa documentação e `mental overload`
- Atividades básicas se tornam lentas e arriscadas ex: refatorar
- Systax switching

```python
rafael = {
    "nome": "rafael",
    "região": "São Paulo",
    "is_cliente": False
    }
```

```python
rafael["is_client"] = True
```

```python
rafael = dict(
    name="rafael",
    region="São Paulo",
    is_cliente=True
)
```

Desafios de escala
  - Como garantir mudaças de `código` e de `dados` no futuro?
  - Como mudar o nome das colunas?
  - Realizar análise estática com `mypy`?
  - Realizar validação desses dados?

## Dataclasse

```python
@dataclasses.dataclasse
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool
```

As Dataclasse nos dão alguns poderes
- Refatorar
- Completar
- Navegar

Comparar `exemplo_06` dict vs dataclasses

Porém...

Quando rodamos em `runtime` , ou seja, estamos `processando` os nossos dados
- Não coneguimos lidar com grandes datasets
- Checar erros dos dados de input
- Detectar durante o processamento
- Checar output antes de salvar
- Usar arquivos de configuração

## Pydantic

Uma maneira de resolver esse problema? `Pydantic`

Substitua esse código

```python
import dataclasses

@dataclass
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool
```

Por esse código

```python
from dataclasses import dataclass

@dataclass
class Cliente:
    """Schema do contrato tabela Cliente"""
    nome: str
    região: str
    is_cliente: bool
```










É uma solução simples e *opensource* e para tornar pipelines baseadas em Dataframes (Pandas e Spark etc) mais seguras, robustas e simples de se trabalhar

*Data validation for scientists, engineers, and analysts seeking correctness.*

Dataframes possuem informação que pandera explicitamente valida em tempo de processamento. Isso é fundamental para pipelines críticas, com Pandera você pode:

1) Definir um contrato de dados

2) Incluir rotinas de validação de tipos e propriedades

3) Integração simples e descomlicada

4) Definir um schema baseado em Pydantic

5) Lazily Validate dataframes assim, você executa todos os testes antes de um erro ser levantado.

6) Integrado com um rico sistema Python como pydantic, fastap, mkdocs, pandas, polars, spark e mypy.

## Instalação

Você pode instalar viar pip:

```bash
pip install pandera
```

ou via poetry

```bash
poetry add pandera
```

### Extras

Instalando funcionalidades adicionais

```bash
pip install pandera[hypotheses]  # hypothesis checks
pip install pandera[io]          # yaml/script schema io utilities
pip install pandera[strategies]  # data synthesis strategies
pip install pandera[mypy]        # enable static type-linting of pandas
pip install pandera[fastapi]     # fastapi integration
pip install pandera[dask]        # validate dask dataframes
pip install pandera[pyspark]     # validate pyspark dataframes
pip install pandera[modin]       # validate modin dataframes
pip install pandera[modin-ray]   # validate modin dataframes with ray
pip install pandera[modin-dask]  # validate modin dataframes with dask
pip install pandera[geopandas]   # validate geopandas geodataframes
```

## Quick Start