from pandera import DataFrameSchema, Column, Check, Index

schema_input = DataFrameSchema(
    columns={
        "Station": Column(
            dtype="string[pyarrow]",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Temperature": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(min_value=-100.0),
                Check.less_than_or_equal_to(max_value=100.0),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(min_value=0.0),
            Check.less_than_or_equal_to(max_value=1_000_000_000),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=False,
    title=None,
    description=None,
)

schema_output = DataFrameSchema(
    columns={
        "Station": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=True,  # Presumindo que cada estação é única no dataset
            coerce=True,
            required=True,
            regex=False,
            description="Nome da estação meteorológica",
            title="Station",
        ),
        "min": Column(
            dtype="float",
            checks=[
                Check.greater_than_or_equal_to(min_value=-100),  # Ajuste conforme a realidade do seu dataset
                Check.less_than_or_equal_to(max_value=100)  # Ajuste conforme a realidade do seu dataset
            ],
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Temperatura mínima registrada na estação",
            title="Min Temperature",
        ),
        "mean": Column(
            dtype="float",
            checks=[
                Check.greater_than_or_equal_to(min_value=-100),  # Ajuste conforme a realidade do seu dataset
                Check.less_than_or_equal_to(max_value=100)  # Ajuste conforme a realidade do seu dataset
            ],
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Temperatura média registrada na estação",
            title="Mean Temperature",
        ),
        "max": Column(
            dtype="float",
            checks=[
                Check.greater_than_or_equal_to(min_value=-100),  # Ajuste conforme a realidade do seu dataset
                Check.less_than_or_equal_to(max_value=100)  # Ajuste conforme a realidade do seu dataset
            ],
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Temperatura máxima registrada na estação",
            title="Max Temperature",
        ),
    },
    checks=None,
    index=Index(
        dtype="int",
        checks=[
            Check.greater_than_or_equal_to(min_value=0),
        ],
        nullable=False,
        coerce=True,
        name=None,
        description="Índice automático gerado pelo DataFrame",
        title="Index",
    ),
    coerce=True,
    strict=False,
    name="WeatherStations",
    description="Schema para dados de estações meteorológicas com temperaturas mínima, média e máxima.",
)