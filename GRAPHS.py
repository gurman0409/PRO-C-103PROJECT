import pandas as pd
import plotly.express as px
df = pd.read_csv("Copy+of+data+-+data.csv")

fig = px.line(df , x = "date" , y = "cases" , color = "country")
fig.show()

fig2 = px.bar(df , x = "date" , y = "cases" , color="country")
fig2.show()

fig3 = px.scatter(df, x = "date" , y = "cases" , size = "cases" , color = "country")
fig3.show()