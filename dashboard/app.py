import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Router Analytics Dashboard")

conn = sqlite3.connect("router_logs.db")

df = pd.read_sql_query("SELECT * FROM query_logs", conn)

if df.empty:
    st.warning("No data yet")
    st.stop()

st.subheader("System Metrics")

total_queries = len(df)
total_cost = df["cost"].sum()
avg_latency = df["latency"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Queries", total_queries)
col2.metric("Total Cost ($)", round(total_cost, 4))
col3.metric("Avg Latency (s)", round(avg_latency, 2))

st.subheader("Model Usage Distribution")

model_counts = df["model_used"].value_counts()

fig, ax = plt.subplots()

ax.pie(model_counts, labels=model_counts.index, autopct="%1.1f%%")

st.pyplot(fig)

st.subheader("Routing Complexity Distribution")

complexity_counts = df["complexity_level"].value_counts()

fig2, ax2 = plt.subplots()

ax2.bar(complexity_counts.index.astype(str), complexity_counts.values)

ax2.set_xlabel("Complexity Level")
ax2.set_ylabel("Query Count")

st.pyplot(fig2)

st.subheader("Latency Distribution")

fig3, ax3 = plt.subplots()

ax3.hist(df["latency"], bins=10)

ax3.set_xlabel("Latency (seconds)")
ax3.set_ylabel("Frequency")

st.pyplot(fig3)

st.subheader("Recent Queries")

st.dataframe(df.tail(10))