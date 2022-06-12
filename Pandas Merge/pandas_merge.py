import pandas as pd 
import numpy as np 

# Dataframe 1
df1 = pd.DataFrame({
		'name': ["tarun", "yogesh", "amit", "vijay","aman"],
		'email':  ["tarun@gmail.com", "yogesh@gmail.com", "amit@gamil.com", "vijay@gmail.com","aman@gmail.com"]
	})

print("############ 1st DataFrame ##############")
print(df1)
print("----------------------------------------")



# Dataframe 2
df2 = pd.DataFrame({
		'name': ["tarun", "yogesh", "amit", "vijay","vipin"],
		'mobile': [9878766545, 9878765654, 3423445544, 3333444556, 9999988888]
	})

print("############ 2nd Mode ##############")
print(df2)
print("----------------------------------------")

# indicator=True will add anw column "_merge" that will indicate the it is "common record" or "from left df" or "from right df"

# Apply merge on two dataframes (By default it will pick the common records from both dataframes)
final_df1 = pd.merge(df1, df2, on='name', indicator=True)
print("############ Default Mode ##############")
print(final_df1)
print("----------------------------------------")

# Apply merge on two dataframes (By default it is same as default mode)
# How="inner" will pick common records from both the dataframe
final_df2 = pd.merge(df1, df2, on='name', how="inner", indicator=True)
print("############ When inner Mode ##############")
print(final_df2)
print("----------------------------------------")

# Apply merge on two dataframes
# How="outer" will pick "common records + left df records + rigth df records" 
final_df2 = pd.merge(df1, df2, on='name', how="outer", indicator=True)
print("############ When  outer Mode ##############")
print(final_df2)
print("----------------------------------------")

# Apply merge on two dataframes
# How="left" will pick "common records + left df records" 
final_df3 = pd.merge(df1, df2, on='name', how="left", indicator=True)
print("############ When left Mode ##############")
print(final_df3)
print("----------------------------------------")

# Apply merge on two dataframes
# How="right" will pick "common records + Right df records" 
final_df4 = pd.merge(df1, df2, on='name', how="right", indicator=True)
print("############ When right Mode ##############")
print(final_df4)
print("----------------------------------------")




# Dataframe 3
df3 = pd.DataFrame({
		'name': ["tarun", "yogesh", "amit", "vijay","aman"],
		'email':  ["tarun@gmail.com", "yogesh@gmail.com", "amit@gamil.com", "vijay@gmail.com", "aman@gmail.com"],
		'mobile': [9878766545, 9878765654, 3423445544, 3333444556, 9999922222]
	})

print("############ 3rd DataFrame ##############")
print(df3)
print("----------------------------------------")

# Dataframe 4
df4 = pd.DataFrame({
		'name': ["tarun", "yogesh", "amit", "vijay","vipin"],
		'mobile': [9878766545, 9878765654, 3423445544, 3333444556, 9999988888],
		'email':  ["tarun@gmail.com", "yogesh@gmail.com", "amit@gamil.com", "vijay@gmail.com", "vipin@gmail.com"]
	})

print("############ 4th Mode ##############")
print(df4)
print("----------------------------------------")


# When both left and right dataframe have some common columns so by default suffix will in (_x,_y for left and right dataframe)
print("############ With default suffix ##############")
final_df5 = pd.merge(df3, df4, on="name", how="outer", indicator=True)
print(final_df5)
print("----------------------------------------")

# When we define suffixes manually
print("############ With defined suffix ##############")
final_df6 = pd.merge(df3, df4, on="name", how="outer", indicator=True, suffixes=('_left','_right'))
print(final_df6)
print("----------------------------------------")


