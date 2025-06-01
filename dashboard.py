import streamlit as st
import pandas as pd
import plotly.express as px

st.title("On-Chain Asset Tracker")

df = pd.read_csv("erc20_data.csv")
df['date'] = pd.to_datetime(df['date'])

metric = st.radio("Select metric", ["volume_usd", "tx_count"])

fig = px.line(df, x="date", y=metric, color="symbol", title=f"Token {metric.replace('_', ' ').title()}")
st.plotly_chart(fig)
