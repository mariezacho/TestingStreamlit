import streamlit as st
import sqlalchemy

# Read the secrets
host = st.secrets["sql"]["host"]
port = st.secrets["sql"]["port"]
database = st.secrets["sql"]["database"]
user = st.secrets["sql"]["user"]
password = st.secrets["sql"]["password"]

# Create the database connection
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = sqlalchemy.create_engine(connection_string)

# Example usage
with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    st.write(result.fetchone())
