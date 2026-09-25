import pandas as pd


df=pd.read_csv("policies.csv")
print(df)



highestCoverage=df["Coverage"].apply(lambda p:p>1000000)
print(highestCoverage)

df["discountedPremium"]=df["Premium"].apply(lambda p:p *9.90)
print(df)
