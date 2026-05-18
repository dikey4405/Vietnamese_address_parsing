import os
print("📂 Current working dir:", os.getcwd())
from sqlalchemy import create_engine, text
import urllib
from config import load_mssql_config

def connect_to_mssql():
    config = load_mssql_config()
    params = urllib.parse.quote_plus(
        f"DRIVER={config['driver']};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"Trusted_Connection=yes;"
    )

    connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(connection_string)
    print("✅ Connected to MSSQL successfully!")
    return engine

if __name__ == '__main__':
    engine = connect_to_mssql()
   