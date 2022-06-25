# ------------------ Delete data from Pandas Dataframe ------------------------------

import pandas as pd
import numpy as np 


path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print("------------------ Main dataframe -------------------")
print(df)
print("--------------------------")
print()

# --------------  1st way of deleting the column using the 'del' method ----------------

# deleting the Age column 
del df['Age']
print(" After deleting the Age column using 'del' method ")
print(df)
df['Age'] = [1,2,3,4,5,6]
print("--------------------------")
print()


# --------------  2nd way of deleting the column using the 'drop' method ----------------

# deleting the single column(Age)
df.drop(['Age'], axis=1, inplace=True)
print(" After deleting the single(Age) column using 'drop' method ")
print(df)
df['Age'] = [1,2,3,4,5,6]
print("--------------------------")
print()

# deleting the multiple columns(Age, Name) 
df.drop(['Age', 'Name'], axis=1, inplace=True)
print(" After deleting the multiple(Age, Name) columns using 'drop' method ")
print(df)
df['Age']  = [1,2,3,4,5,6]
df['Name'] = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6']
print("--------------------------")
print()

# Removing columns on index basis using drop function
path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
df.drop(df.columns[[0, 3]], axis=1, inplace=True)
print(" After deleting the multiple(Age, Name) columns using 'drop' method by passing index ")
print(df)
df.insert(2, 'Age', [1,2,3,4,5,6])
df.insert(0, 'Name', ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6'])
print("--------------------------")
print()

# Using loc with drop to remove columns
# Removing all columns between a starting column to another column
# Following code will delete the columns from 'Date Of Birth' to 'Address'
# Note: loc will include last column for delete operation
df.drop(df.loc[:, 'Date of Birth':'Address' ], axis=1, inplace=True)
print(" After deleting the multiple(Date Of Birth, Address) columns using 'drop' method by passing column names in loc function ")
print(df)
df.insert(1, 'Date of Birth', ['01-07-2022', '02-07-2022', '03-07-2022', '04-07-2022', '05-07-2022', '06-07-2022',])
df.insert(2, 'Address', ['Alwar', 'Jaipur', 'Behror', 'Alwar', 'Kota', 'Bhiwadi'])
print("--------------------------")
print()

# Using iloc with drop to remove columns
# Removing all columns between a starting column to another column
# Following code will delete the columns at index 1(Date Of Birth) and 2(Address)
# Note: iloc will exclude last index column for delete operation
df.drop(df.iloc[:, 1:3], axis=1, inplace=True)
print(" After deleting the multiple(Date Of Birth, Address) columns using 'drop' method by passing index range in iloc function ")
print(df)
df.insert(1, 'Date of Birth', ['01-07-2022', '02-07-2022', '03-07-2022', '04-07-2022', '05-07-2022', '06-07-2022',])
df.insert(2, 'Address', ['Alwar', 'Jaipur', 'Behror', 'Alwar', 'Kota', 'Bhiwadi'])
print("--------------------------")
print()

# ------------ 3rd Way of deleting column using pop method ------------------

# deleting the 'Address' column 
print(" After deleting the 'Address' columns using 'pop' method")
# pop method returns the deleted column data
column_data=df.pop('Address')
print(df)
print("------------- Column data -------- \n ",column_data)
df.insert(2, 'Address', ['Alwar', 'Jaipur', 'Behror', 'Alwar', 'Kota', 'Bhiwadi'])
print("--------------------------")
print()