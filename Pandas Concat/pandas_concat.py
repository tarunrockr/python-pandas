import pandas as pd
import numpy as np 


# Dataframe 1
india_weather_df =pd.DataFrame({
		'place': ['delhi', 'jaipur', 'chandigarh'],
		'temperature': [34,45,22],
		'wind': [12,23,19]
	})

# Dataframe 2
uk_weather_df =pd.DataFrame({
		'place': ['liverpool', 'manchester', 'bristol'],
		'temperature': [32,41,39],
		'wind': [11,18,21]
	})


# Concatening the records of two dataframe by the use of concat method (We can concat more than two dataframes)
# df = pd.concat([india_weather_df, uk_weather_df])
# print(df)

# df = pd.concat([india_weather_df, uk_weather_df], ignore_index=True)
# print(df)

# We can pass keys for each subset dataframes
df = pd.concat([india_weather_df, uk_weather_df], keys=['india','uk'])
print(df)
print("------------------")

print(df.loc['india'])
print("------------------")

print(df.loc['uk'])
print("------------------")


# Sub DataFrame 1
df1 = pd.DataFrame({
		'place': ['delhi', 'jaipur', 'chandigarh'],
		'temperature': [34,45,22]
	}, index=[0,1,2])

# Sub DataFrame 2
df2 = pd.DataFrame({
		'place': ['delhi', 'jaipur', 'chandigarh'],
		'wind': [11,18,21]
	})

df3 = pd.DataFrame({
		'place': ['chandigarh','jaipur'],
		'wind': [18,21]
	},  index=[2,1])

# # Concatenating dataframe 1 and dataframe 2 by column using axis=1 
# final_df = pd.concat([df1, df2], axis=1)
# print(final_df)
# print("------------------")

# Concatenating dataframe 1 and dataframe 3 by column using axis=1 , To match the columns we have added index parameter in dataframe.
final_df = pd.concat([df1, df3], axis=1)
print(final_df)
print("------------------")

# Creating an event series and concatening it to existing dataframe
series1 = pd.Series(["clear", "cloudy", "rainy"], name="event")

# Concatening eries to existing dataframe
dfs = pd.concat([df1, series1], axis=1)
print(dfs)


