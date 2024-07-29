import streamlit as st
import sqlalchemy
import pymysql
pymysql.install_as_MySQLdb()

# Then you can use SQLAlchemy as usual
from sqlalchemy import create_engine
import pandas as pd

def get_customers():
    # Read the secrets
    host = st.secrets["sql"]["host"]
    port = st.secrets["sql"]["port"]
    database = st.secrets["sql"]["database"]
    user = st.secrets["sql"]["user"]
    password = st.secrets["sql"]["password"]

    # Create the database connection string
    connection_string = f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}"
    
    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    # Define the query
    query = "SELECT id, name FROM connect.operators"

    try:
        # Execute the query and fetch data
        with engine.connect() as connection:
            data = pd.read_sql(query, connection)
            # Set the index to 'id'
            data = data.set_index('id')
            return data

    except sqlalchemy.exc.OperationalError as e:
        st.error(f"OperationalError: {e}")
        return None

    except sqlalchemy.exc.SQLAlchemyError as e:
        st.error(f"SQLAlchemyError: {e}")
        return None

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
cos = get_customers()
st.write(cos)