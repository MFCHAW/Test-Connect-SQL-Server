import streamlit as st
import pyodbc

# Initialize connection
# Uses st.cache_resource to only run once


# @st.experimental_memo
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=LINTRAMAX154\LMONE;DATABASE=mydb;UID=PMSUser;PWD=lmone2014"
    )

    # return pyodbc.connect(
    #     "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    #     + st.secrets["server"]
    #     + ";DATABASE="
    #     + st.secrets["database"]
    #     + ";UID="
    #     + st.secrets["username"]
    #     + ";PWD="
    #     + st.secrets["password"]
    # )


conn = init_connection()

# Perform query
# Uses st.cache_data to only rerun when the query changes or after 10 min


# @st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query('Select * from mytable;')

# Print results
for row in rows:
    st.write(f'{row[0]} has a :{row[1]}:')
