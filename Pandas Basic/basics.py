import pandas as pd 
import numpy as np 


# Creating the dataframe from existing excel file
path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print(df)

# # Creating the dataframe from existing csv file
# path = "sample_csv.csv"
# df = pd.read_csv(path)
# print(df)

# # Creating pandas dataframe using dictionary 
# sample_dict = {
# 				'Name': ["Ajay", "Amit", "Vijay", "Tarun", "Yogesh", "Yash"],
# 				'Date of Birth': ["10-04-1991", "15-03-1992", "03-07-1995", "29-10-1997", "21-12-1999", "20-01-2000"],
# 				'Address': ["Bhiwadi", "Ajmer", "Jaipur", "Behror", "Alwar", "Kota"],
# 				'Age': [1, 10, 15, 20, 23, 25] 
# 			  }

# df = pd.DataFrame(sample_dict)
# print(df)


# # To check no of rows and columns in the dataframe we use shape property, It return rows and column values in tuple form
# sh = df.shape
# print("No. of rows: ", sh[0])
# print("No. of columns: ", sh[1])

# rows, columns = df.shape
# print("No. of rows: ", rows)
# print("No. of columns: ", columns)

# # To print some starting rows from dataframe we use df.head(). No. of rows can be provided as head function parameter
# print(df.head(3))

# # To print some last rows from dataframe we use df.tail(). No. of rows can be provided as tail function parameter
# print(df.tail(3))

# -------------------  Slicing operation ------------------------------

# # Printing 3rd and 4th rows only from dataframe
# print(df[3:5])

# # Printing all the data from dataframe
# print(df[:])
# print(df)

# # To get Column names we use df.columns
# print(df.columns)

# -------------------- Fetch selected columns -----------------

# # To get column values we use like df.column_name or df['column_name']
# print(df.Address)
# print(df['Address'])

# # To get multiple column values from dataframe we use like df[ ['col1_name','col2_name'] ]
# print( df[ ['Name', 'Address'] ] )

# -------------------- Fetch selected columns with conditions -----------------

# print(df['Age'][ df['Age'] > 20])  # To fetch only age column with condtion on Age
# print(df[df['Age'] > 20]['Age'])   # To fetch only age column with condtion on Age

# print(df[df['Age'] > 20][['Age','Name']]) # To fetch age and name columns with condtion on Age

# print(df[ df['Age'] ==  df['Age'].max() ])  # or print(df[ df.Age ==  df.Age.max() ]) To fetch max age person data
# print(df['Age'].max())  # To fetch max age
# print(df['Age'].min())  # To fetch min age
# print(df['Age'].mean()) # To fetch mean value of age
# print(df['Age'].std()) # To fetch standard deviation of age
# print(df.describe()) # To describe the dataframe


#  -------------------- Setting the column as index --------------------

# # Setting the Age column as index and Make this change to original copy by setting inplace = True
# df.set_index('Age', inplace = True)

# # Resetting index. drop=True will not save it in different column and will change it in original column
# df.reset_index(drop=True ,inplace=True)
# print(df)


# -------------------  Check Data Type ------------------------------

# # To check the type of column
# print(type(df['Name']))

# # To print a list datatypes of all columns of dataframe
# print("Data Type of all columns: ",df.dtypes)

# # To print datatype of a particular column
# print("Data Type of Name column: ",df.Name.dtypes)


