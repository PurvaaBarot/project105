import math
import plotly_express as px
import pandas as pd

df=pd.read_csv("p105.csv")

mean=df["Numbers"].mean()

x=df["Numbers"]
squares=[]

for i in x :
    d=i-mean
    squares.append(d**2)

total=0
for i in squares :
    total+=i

a=total/(len(x)-1)

std=math.sqrt(a)
print(std)
print(df["Numbers"].std())