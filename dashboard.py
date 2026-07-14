import streamlit as st
import sqlite3
import pandas as pd


DB = "vagas.db"


def carregar_dados():

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query("SELECT * FROM vagas ORDER BY score DESC", conn)

    conn.close()

    return df


st.set_page_config(page_title="Auto Currículo", layout="wide")

st.title("🚀 Auto Currículo - Dashboard")

df = carregar_dados()

st.metric("Total de vagas", len(df))
st.metric("Score médio", round(df["score"].mean(), 2))

st.dataframe(df, use_container_width=True)

st.bar_chart(df["score"])