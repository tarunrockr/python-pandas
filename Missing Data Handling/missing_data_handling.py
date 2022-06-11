import pandas as pd
import numpy as np 

# # Reading weather csv file in dataframe
# path = "../sample_files/InputFiles/weather.csv"
# # parse_date is for converting date to timestamp
# df = pd.read_csv(path, parse_dates=['Date'])
# # print(df)
# # print(type(df['Date'][0]))


# # Replacing NaN value to some other value using fillna function and creating new datafrane with replaced values
# df_new = df.fillna(0)
# print(df_new)


# # Replacing column NaN values to some other values columnwise and creating new dataframe with replaced values
# df_new = df.fillna({
# 		'Min Temperature': 0.0,
# 		'Max Temperature': 0.0,
# 		'Event': 'No Data' 
# 	})
# print(df_new)


# # Replacing column NaN values to previous column values and creating new dataframe with replaced values
# df_new = df.fillna(method="ffill")
# print(df_new)

# # Replacing column NaN values to upcoming column values and creating new dataframe with replaced values
# df_new = df.fillna(method="bfill")
# print(df_new)

# # Replacig NULL values based on specific method using interpolate
# # dataframe.interpolate(method, axis, inplace, limit, limit_direction, limit_area, downcast, kwargs)
# new_df = df.interpolate( method="ffill")
# print(new_df)


# # Droping the rows which has NaN values
# print(df)
# new_df = df.dropna()
# print(new_df) 


# # Droping only those rows which has all column as NaN(blank) values
# print(df)
# new_df = df.dropna(how="all")
# print(new_df)

# # Keep only those rows which has atleat 3 column values as non NaN(blank) otherwise it will be dropped (so threshold will be 3 here)
# print(df)
# new_df = df.dropna(thresh=3)
# print(new_df) 




# --------------------------------------------------------------------



# path = "../sample_files/InputFiles/weather1.csv"
# # parse_date is for converting date to timestamp
# dataframe = pd.read_csv(path, parse_dates=['Date'])
# #print(dataframe)


# # Replacing some specific values by replace method
# dataframe = dataframe.replace(-111111, np.NaN)
# print(dataframe)

# # Replacing set of specific values in dataframe
# dataframe = dataframe.replace([-111111, -222222], np.NaN)
# print(dataframe)

# # Replacing column values in dataframe
# dataframe = dataframe.replace({
# 	'Min Temperature': -111111,
# 	'Max Temperature': [-111111, -222222],
# 	'Event': 0
# 	}, np.NaN)
# print(dataframe)

# # Replacing value to some other values in the form of dictionary with replace method
# dataframe = dataframe.replace({
# 		-111111: np.NaN,
# 		-222222: np.NaN,
# 		"clear": "more clear" 
# 	})
# print(dataframe)

# # Replacing alphabatical value of a cell to balnk or some other values using regular expression in regular method
# print(dataframe)
# dataframe = dataframe.replace({
# 	'Min Temperature': '[A-Za-z]',
# 	'Max Temperature': '[A-Za-z]' 
# 	}, '', regex=True)
# print(dataframe)

# ------------------------------------
players_dataframe = pd.DataFrame({
	'name': ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8'],
	'ranking': ['good', 'average', 'poor', 'excellent', 'outstanding', 'average', 'poor', 'excellent' ]
	})

players_dataframe = players_dataframe.replace(['good', 'average', 'poor', 'excellent', 'outstanding'], ['2 star', '3 star', '1 star', '4 star', '5 star'])

print(players_dataframe)



