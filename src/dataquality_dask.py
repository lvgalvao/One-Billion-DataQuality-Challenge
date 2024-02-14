from pathlib import Path
import dask
dask.config.set({'dataframe.query-planning': True})
import dask.dataframe as dd # noqa
import pandera as pa # noqa

from schema.measurements import schema_input, schema_output # noqa

@pa.check_output(schema_input, lazy=True)
def retrieve_weather_stations(path: Path) -> dd.DataFrame:
    return dd.read_csv(path=path, sep=";")

@pa.check_output(schema_output, lazy=True)
def calculate_weather_stations(dataframe = dd.DataFrame) -> dd.DataFrame:
    dataframe_groypby = dataframe.groupby("Station")['Temperature'].agg(['max', 'min', 'mean']).reset_index()
    result_df = dataframe_groypby.compute().sort_values("Station")
    return result_df

def main() -> None:

    dataset_path = Path().absolute() / "data"
    try:
        df_measurements = retrieve_weather_stations(dataset_path / "measurements.txt")
    except pa.errors.SchemaErrors as err:
        print("Validation errors occurred at df_measurements")
        print(err.failure_cases)  # Imprime os casos de falha detalhados

    try:
        result_df = calculate_weather_stations(df_measurements)
    except pa.errors.SchemaErrors as err:
        print("Validation errors occurred at df_result")
        print(err.failure_cases)  # Imprime os casos de falha detalhados

    print(result_df)

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    took = time.time() - start_time
    print(f"Dask Took: {took:.2f} sec")
