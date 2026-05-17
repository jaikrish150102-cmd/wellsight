import streamlit as st
import pandas as pd
import plotly.express as px

st.title("WellSight 🛢️")
st.write("Oil & Gas Production Analytics Dashboard")

df = pd.read_csv("oil-and-gas-annual-production-beginning-2001-1.csv")
df["Oil Produced, bbl"] = df["Oil Produced, bbl"].fillna(0)
df["Gas Produced, Mcf"] = df["Gas Produced, Mcf"].fillna(0)
df["Water Produced, bbl"] = df["Water Produced, bbl"].fillna(0)

st.sidebar.title("🔍 Filters")
years = sorted(df["Reporting Year"].dropna().unique())
selected_year = st.sidebar.selectbox("Select Year", ["All"] + [str(y) for y in years])
counties = sorted(df["County"].dropna().unique())
selected_county = st.sidebar.selectbox("Select County", ["All"] + list(counties))

if selected_year != "All":
    df = df[df["Reporting Year"] == int(selected_year)]
if selected_county != "All":
    df = df[df["County"] == selected_county]

st.subheader("📊 Key Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Wells", f"{len(df):,}")
col2.metric("Total Oil (bbl)", f"{df['Oil Produced, bbl'].sum():,.0f}")
col3.metric("Total Gas (Mcf)", f"{df['Gas Produced, Mcf'].sum():,.0f}")

st.divider()

st.subheader("🏆 Top 10 Oil Producing Counties")
county_oil = df.groupby("County")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(10).reset_index()
fig1 = px.bar(county_oil,
              x="County",
              y="Oil Produced, bbl",
              title="Top 10 Counties by Oil Production",
              color_discrete_sequence=["#FFA500"])
st.plotly_chart(fig1)

st.divider()

st.subheader("📈 Oil Production Trend Over Years")
year_oil = df.groupby("Reporting Year")["Oil Produced, bbl"].sum().reset_index()
fig2 = px.line(year_oil,
               x="Reporting Year",
               y="Oil Produced, bbl",
               title="Production Trend 2001 to Present",
               color_discrete_sequence=["#FFD700"])
st.plotly_chart(fig2)

st.divider()

st.subheader("🥧 Top 5 Counties Production Share")
county_pie = df.groupby("County")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(5).reset_index()
fig3 = px.pie(county_pie,
              values="Oil Produced, bbl",
              names="County",
              title="Production Share",
              color_discrete_sequence=px.colors.sequential.Oranges)
st.plotly_chart(fig3)

st.divider()

st.subheader("🏢 Top 10 Oil Producing Companies")
company_oil = df.groupby("Company Name")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(10).reset_index()
fig4 = px.bar(company_oil,
              x="Oil Produced, bbl",
              y="Company Name",
              title="Top Companies by Oil Production",
              orientation='h',
              color_discrete_sequence=["#FF6B00"])
st.plotly_chart(fig4)