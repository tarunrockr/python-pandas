import pandas as pd 
import numpy as np 



# Reading the csv file
path = "../sample_files/InputFiles/crosstab_file.csv"
df = pd.read_csv(path)
print(df)
print("-----------------")

# Syntax: pandas.crosstab(index, columns, values=None, rownames=None, 
#  colnames=None, aggfunc=None, margins=False, margins_name=’All’, dropna=True, normalize=False)

# Get crosstab dataframe of number of types citywise
new_df = pd.crosstab(df.City, df.Type)
print("Number of types citywise: \n")
print(new_df)
print("-----------------")

# Get crosstab dataframe of number of types of people with citywise (Adding name in row)
new_df = pd.crosstab([df.City, df.Name], df.Type)
print("Number of types of people with citywise: \n")
print(new_df)
print("-----------------")

# Get crosstab dataframe of number of types of people with citywise (Adding name in column)
new_df = pd.crosstab(df.City, [df.Type, df.Name])
print("Number of types of people with citywise: \n")
print(new_df)
print("-----------------")

# We can supply margins = True to get total value( A new all column will be added )
new_df = pd.crosstab(df.City, df.Type, margins=True)
print("Number of types citywise: \n")
print(new_df)
print("-----------------")

# By normalize='index' we can get the percentage part
new_df = pd.crosstab(df.City, df.Type, normalize='index')
print("Number of types citywise: \n")
print(new_df)
print("-----------------")

# aggfunc function to get aggregated values using supplied values in 'values' parameter
new_df = pd.crosstab(df.Gender, df.Type, values=df.Age, aggfunc=np.average)
print("Number of types citywise: \n")
print(new_df)
print("-----------------")