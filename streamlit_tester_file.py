import streamlit as st

# Initialize connection.
conn = st.connection('mariadb', type='sql')

# Perform query.
df = conn.query('SELECT * from connect.location;', ttl=600)

# Print results.
print(df)
