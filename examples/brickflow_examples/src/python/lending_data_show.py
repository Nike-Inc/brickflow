from brickflow.context import ctx


def lending_data_print():
    ctx.spark.sql(
        """
        SELECT
        addr_state, *
        FROM
        parquet.`dbfs:/databricks-datasets/samples/lending_club/parquet/` limit 10
    """
    ).show(truncate=False)


if __name__ == "__main__":
    lending_data_print()
