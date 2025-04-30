
from snowflake.snowpark import Session
from snowflake.connector.pandas_tools import write_pandas
from snowflake_config import SNOWFLAKE_CONFIG

def create_snowflake_session():
    session = Session.builder.configs(SNOWFLAKE_CONFIG).create()
    return session

def upload_dataframe_to_snowflake(session, df, table_name):
    conn = session._conn  # conexión subyacente del conector Snowflake
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name)
    if success:
        print(f"Successfully uploaded {nrows} rows to {table_name}")
    else:
        raise RuntimeError(f"Failed to upload data to {table_name}")

