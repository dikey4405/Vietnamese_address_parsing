import pandas as pd
from sqlalchemy import create_engine
from config import load_mssql_config
from connect import connect_to_mssql

def extract_vietnamese_administrative_units_data_from_db():
    conn = connect_to_mssql()
        # Extract data from MSSQL database
    try:
        VN_address_df = pd.read_sql(
            'SELECT p.name, p.full_name, d.name, d.full_name, w.name, w.full_name\
            FROM dbo.wards as w, dbo.districts as d, dbo.provinces as p \
            WHERE w.district_code = d.code AND d.province_code = p.code'
            , con=conn)
    except Exception as e:
            print(f"An error occurred: {e}")  

    return VN_address_df

if __name__ == '__main__':
    extract_vietnamese_administrative_units_data_from_db()