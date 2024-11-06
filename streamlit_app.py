# streamlit_app.py 
#作成アプリの中身 #この例はただのデータフレーム表示アプリ

import streamlit as st

from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session

# secrets.tomlの内容を直接参照
connection_parameters = {
    "account": st.secrets["connections"]["snowflake"]["account"],
    "user": st.secrets["connections"]["snowflake"]["user"],
    "password": st.secrets["connections"]["snowflake"]["password"],
    "role": st.secrets["connections"]["snowflake"]["role"],
    "warehouse": st.secrets["connections"]["snowflake"]["warehouse"],
    "database": st.secrets["connections"]["snowflake"]["database"],
    "schema": st.secrets["connections"]["snowflake"]["schema"]
}

session = Session.builder.configs(connection_parameters).create()

# sql = "SELECT * FROM TEST_WEB LIMIT 10"
# df = session.sql(sql).to_pandas()
# st.write(df)



# 読み込んだデータをデータフレームに
st.write("TEST:balloon:読み込んだデータをデータフレームに")

sql = "SELECT * FROM TEST_WEB LIMIT 10"
df = session.sql(sql).to_pandas()
# データフレーム表示
st.write(df)

# 読み込んだデータをグラフ化
st.subheader("TEST:balloon:読み込んだデータをグラフ化")
st.bar_chart(data=df, x="ABC", y="RANDUM")
