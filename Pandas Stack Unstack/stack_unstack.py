import numpy as np 
import pandas as pd 


# Read csv file 
path = "../sample_files/InputFiles/stack_unstack_weather.xlsx"
df = pd.read_excel(path, header=[0,1])
print(df)
print("--------------")

# Stack the dataframe (By default it takes inner most level to stack df here it is header 1)
stack_df = df.stack()
print(stack_df)
print("--------------")

# We can supply the level 
stack_df1 = df.stack(level=0)
print(stack_df1)
print("--------------")


# Unstack is the reverse process of stack
unstack_df = stack_df.unstack()
print(unstack_df)
print("--------------")

unstack_df1 =  stack_df1.unstack()
print(unstack_df1)
print("--------------")
