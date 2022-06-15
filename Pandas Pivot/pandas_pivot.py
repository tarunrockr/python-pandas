import pandas as pd 
import numpy as np 

# Reading the csv file and creating dataframe
path = "../sample_files/InputFiles/weather2.csv"
df = pd.read_csv(path)
print(df)
print("--------------")

# Use of pivot function to reshape given dataframe (Pivot does not support data aggregation)
new_df = df.pivot(index="Date", columns="Place")
print("Rehaped Pivot Table: ", new_df)
print("--------------")

# If we want to get some specific column values then we can pass column name in values argument
new_df1 = df.pivot(index="Date", columns="Place", values="Min Temperature")
print(new_df1)
print("--------------")

# If we want to get some specific column values then we can pass column name in values argument
new_df2 = df.pivot(index="Date", columns="Place", values=["Min Temperature", "Max Temperature"])
print(new_df2)
print("--------------")


# ------------------  pivot_table --------------------------- #
# By using pivot_table we can summarize and aggregate dataframe values
path1 = "../sample_files/InputFiles/weather3.csv"
print("-----------  2nd Dataframe ------------")
df2 = pd.read_csv(path1)
print(df2)
print("--------------")

# By default it will calculate the average of values
pv_df = df2.pivot_table(index="Date", columns="Place")
print(pv_df)
print("--------------")

# Passing aggfunc for type of aggregate function
pv_df2 = df2.pivot_table(index="Date", columns="Place", aggfunc="sum")
print(pv_df2)
print("--------------")

# Passing aggfunc for type of aggregate function
pv_df3 = df2.pivot_table(index="Date", columns="Place", aggfunc="count")
print(pv_df3)
print("--------------")

# To get the margins between average values 
pv_df4 = df2.pivot_table(index="Date", columns="Place", margins=True)
print(pv_df4)
print("--------------")


# ------------------  pivot_table Grouper --------------------------- #

path2 = "../sample_files/InputFiles/weather4.csv"
print("-----------  3rd Dataframe ------------")
df3 = pd.read_csv(path2)
print(df3)
print("--------------")


df3['Date'] = pd.to_datetime(df3['Date'])

pv_df5= df3.pivot_table(index=pd.Grouper(freq='M', key="Date" ), columns="Place")
print(pv_df5)

