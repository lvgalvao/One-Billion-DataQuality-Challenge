# DataQuality e DataOPS

Como validar 1 bilhão de linhas?

## Plano de aula

Dia 24/09 ás 9 horas pelo Zoom

`9h00 - 9h10: Contexto DataQuality`
- Principais desafios
- Oportunidades na área
- Mercado

`9h10 - 9h25: Desafio de Negócios`
- Como lidar com inconsistência no banco de dados e em APIs

`9h25 - 10h25: Data Quality em 1 Bilhão de Linhas com Python + Pydantic`
- Live code (Git e Github, Python e Pydantic)
  
`10h25 - 10h45: Intervalo`

`10h45 - 11h05: Documentação`
- Demonstração de como documentar contrato de dados no Mkdocs.

`11h05 - 12h25: Data Quality em 1 Bilhão de Linhas com Pandera`
- Live code (Pandera e duckdb)

`12h22 - 12h50: Sorteio de brindes e sessão de Dúvidas (30 minutos)`
- Sorteio de brindes
- Sorteio de mentoria
- Espaço aberto para perguntas e esclarecimentos e discussão de casos específicos trazidos pelos participantes.

## Preparação

Assistir a série de vídeos `Como instalar Python em 2024`

`vídeo 01` - [Como instalar Python em 2024 + VSCode, Git e Github do Zero](https://www.youtube.com/watch?v=-M4pMd2yQOM)

`vídeo 02` - [Como instalar Python em 2024 + Pyenv, PIP, VENV, PIPX e Poetry](https://www.youtube.com/watch?v=9LYqtLuD7z4)

## Desafio de Negócios

Este projeto aborda o desafio de processar e validar eficientemente um conjunto de dados extremamente grande, especificamente um arquivo contendo aproximadamente 1 bilhão de registros de temperatura de várias estações meteorológicas, totalizando cerca de 14GB. Inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), proposto originalmente para a linguagem Java, este projeto adapta o desafio para Python, demonstrando a capacidade de Python em manipular e analisar dados em grande escala.

Os dados representam medições de temperatura de várias estações meteorológicas em um formato simples: `<nome da estação>;<medição da temperatura>`, com as temperaturas apresentadas com precisão de uma casa decimal.

**Exemplo de Dados:**

```python-repl
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
...
```

O objetivo é ler esses dados, calcular a temperatura mínima, média e máxima para cada estação e apresentar os resultados de forma ordenada pelo nome da estação.

## Destaques do Projeto

* **Leitura e Processamento Eficiente**: Utiliza a biblioteca Dask para processamento paralelo de dados, permitindo a manipulação eficiente de datasets que ultrapassam a capacidade de memória RAM disponível.
* **Validação Robusta de Dados**: Aplica a biblioteca Pandera para assegurar a integridade e a validade dos dados através de esquemas de validação, garantindo a qualidade dos resultados.
* **Cálculo de Estatísticas Meteorológicas**: Realiza a agregação dos dados para calcular as temperaturas mínima, média e máxima para cada estação meteorológica, oferecendo insights valiosos sobre as variações climáticas.

## Pré-requisitos

Para executar este projeto, é necessário ter Python 3.6 ou superior. As seguintes bibliotecas são essenciais:

* Dask: Para o processamento paralelo e eficiente de grandes volumes de dados.
* Pandera: Para a validação de esquemas dos datasets processados.

**Instalação das Dependências:**

```bash
pip install dask pandera
```

## Uso

Coloque o arquivo de dados no diretório `data/` e execute o script `main.py` para iniciar o processamento:

```bash
python main.py
```

Assegure-se de que o arquivo de dados siga o formato especificado, com os registros separados por `;` e as informações corretas de nome da estação e temperatura.

## Estrutura do Código

* `main.py`: O script principal que coordena a leitura, validação e cálculo das estatísticas meteorológicas.
* `schema/measurements.py`: Contém os esquemas de entrada e saída definidos com Pandera, usados para validar a estrutura dos dados processados.
* `data/`: O diretório onde os arquivos de dados brutos devem ser armazenados antes da execução do script.

Ao enfrentar o desafio de validar e processar um volume massivo de dados, este projeto ilustra o poder do Python em lidar com análises de dados em larga escala, provendo uma solução robusta e eficiente para a análise meteorológica.

## Próximos passos

Esse projeto faz parte da *Jornada de Dados*
Nossa missão é fornecer o melhor ensino em engenharia de dados

Se você quer:

- Aprender sobre Duckdb e engenharia de dados
- Construir uma base sólida em Python e SQL
- Criar ou melhorar seu portfólio de dados
- Criar ou aumentar o seu networking na área
- Mudar ou dar o próximo passo em sua carreira

A Jornada de Dados é o seu lugar

[![Imagem](https://github.com/lvgalvao/data-engineering-roadmap/raw/main/pics/jornada.png)](https://www.jornadadedados2024.com.br/workshops)

Para entrar na lista de espera clique no botao

[![Imagem](https://raw.githubusercontent.com/lvgalvao/data-engineering-roadmap/main/pics/lista_de_espera.png)](https://forms.gle/hJMtRDP3MPBUGvwS7?orbt_src=orbt-vst-1RWyYmpICDu9gPknLgaD)