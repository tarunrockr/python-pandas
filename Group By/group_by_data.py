import pandas as pd
import numpy  as np 


# Reading weather_group_data csv files 
path = "../sample_files/InputFiles/weather_group_data.csv"
df = pd.read_csv(path)
print(df)

# Getting the group by data on place, It will return a DataFrameGroupBy object
groupby_df_object = df.groupby('Place')
print(groupby_df_object)

# Iterating over groupby_df_object using for loop

for place, place_df in groupby_df_object:

	print("Place: ",place)
	print("Place dataframe: ", place_df)
	print("----------------------------")


# We can also get a specific group dataframe by just passing the place name as key
delhi_df = groupby_df_object.get_group('Delhi')
print("Delhi DataFrame: ", delhi_df)
jaipur_df = groupby_df_object.get_group('Jaipur')
print("Jaipur DataFrame: ", jaipur_df)


# fetching the aggregated max value group wise
print("Maximum values from each group")
print(groupby_df_object.max())

# fetching the aggregated min value group wise
print("Minimum values from each group")
print(groupby_df_object.min())

# fetching the aggregated average value group wise
print("Average values from each group")
print(groupby_df_object.mean())

# fetching the desritedinfo form each group
print("Average values from each group")
print(groupby_df_object.describe())

