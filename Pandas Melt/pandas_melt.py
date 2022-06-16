import numpy as np
import pandas as pd 


# Reading csv data 
path = "../sample_files/InputFiles/city_weekly_temperature.csv"
df = pd.read_csv(path)
print(df)
print("---------------------------------------")

# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)

new_df = pd.melt(df, id_vars="day")
print(new_df) 
print("---------------------------------------")

new_df1 = new_df[ new_df["variable"] == "Jaipur" ]
print(new_df1)
print("---------------------------------------")

new_df2 = pd.melt(df, id_vars="day", var_name="city", value_name="city_temperature")
print(new_df2)
print("---------------------------------------")

new_df3 = new_df2[ new_df2["city"] == "Delhi" ]
print(new_df3)

