import pandas as pd
import plotly.express as px

# Load and clean data
df = pd.read_csv("oil-and-gas-annual-production-beginning-2001-1.csv")
df["Oil Produced, bbl"] = df["Oil Produced, bbl"].fillna(0)

# Top 10 counties by oil production
county_oil = df.groupby("County")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(10).reset_index()

# Create bar chart
fig = px.bar(county_oil, 
             x="County", 
             y="Oil Produced, bbl",
             title="Top 10 Oil Producing Counties")

fig.write_html("chart1.html")
print ("Chart saved! Open chart.html to see it.")

# production by year
year_oil = df.groupby("Reporting Year")["Oil Produced, bbl"].sum().reset_index()

fig2 = px.bar( year_oil,
               x= "Reporting Year",
               y="Oil Produced, bbl",
               title="Oil production trend 2001 to present"  )

fig2.write_html("Chart2.html")
print("Chart 2 saved")

Company_oil= df.groupby("Company Name")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(10).reset_index()

fig3 = px.bar(Company_oil,
              x= "Oil Produced, bbl",
              y= "Company Name",
              title= "Top 10 oil companies",
              orientation="h")

fig3.write_html("chart3.html")
print("Chart 3 ready")

county_pie = df.groupby("County")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(5).reset_index()

fig4 = px.pie(county_pie,
              values="Oil Produced, bbl",
              names="County",
              title="Top Oil production companies")

fig4.write_html("chart4.html")
print("Chart 4 ready")