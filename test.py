import pandas as pd

df = pd.read_csv("oil-and-gas-annual-production-beginning-2001-1.csv")

print(df.head())
print(df.columns)
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print("Information:", df.info())

df["Gas Produced, Mcf"] = df["Gas Produced, Mcf"].fillna(0)
df["Oil Produced, bbl"] = df["Oil Produced, bbl"].fillna(0)
df["Water Produced, bbl"] = df["Water Produced, bbl"].fillna(0)
print("Information:", df.info())

print("Data cleaned!")

#Top 11 countries in oil production
County_oil= df.groupby("County")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(11)
print(County_oil)

#Top 3 companies in Oil production
County_oil= df.groupby("Company Name")["Oil Produced, bbl"].sum().sort_values(ascending=False).head(3)
print(County_oil)

#Top oil production by year
County_oil= df.groupby("Reporting Year")["Oil Produced, bbl"].sum().sort_values(ascending=True).head(5)
print(County_oil)

#How many wells does each company have
County_oil= df.groupby("Company Name")["API Well Number"].count().sort_values(ascending=False).head(10)
print(County_oil)

#Average oil producing country
County_oil= df.groupby("County")["API Well Number"].mean().sort_values(ascending=False).head(10)
print(County_oil)
