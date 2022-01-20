import plotly_express as px
import pandas as pd

df=pd.read_csv("p105.csv")

mean=df["Numbers"].mean()
print(mean)