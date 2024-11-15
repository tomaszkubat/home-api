import streamlit as st
import pandas as pd

# TODO pin the proper data source
def get_tasks_data():
    df = pd.DataFrame({
        "id": [1,2,3,4,5,6,7],
        "user": ["A","A","B","B","A","C","C"],
        "type": [1,2,1,1,3,4,3],
        "description": ["lorem","ipsum","dolor","sit","amet","consectetur","adipiscing"]
        
    })
    return df


st.write("### Test tasks data", get_tasks_data())

# db = DB("db/data.db")
# db.connect()