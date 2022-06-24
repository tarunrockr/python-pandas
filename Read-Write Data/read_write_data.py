import numpy as np 
import pandas as pd 


# ----------------- Reading csv file with header ------------------

# path = "../sample_files/data.csv"
# df = pd.read_csv(path)
# df = pd.read_csv(path, skiprows=1) # skiprows is to skip first row
# df = pd.read_csv(path, header=1) # header is pointing to second row
# df = pd.read_csv(path, header=1, nrows=3) # we use nrows to read n number of rows
# print(df)

# # ---------------- Rading csv file without header ---------------
# path = "../sample_files/data_without_header.csv"
# # df = pd.read_csv(path, header=None) # With header = None it will pick 0,1,2,3.. as column names
# df = pd.read_csv(path, header=None, names=["Name", "Date of birth", "Address", "Roll"]) # We use names to specify column names
# print(df)

# --------------  Use of na_values property ---------------------

# # When we want to replace some existing values with NaN then we can use na_values
# df = pd.read_csv(path, na_values=["not available", "n.a."])
# print(df)

# # When we want to replace some existing values columnwise with NaN the we can use na_values
# df = pd.read_csv(path, na_values={ 
# 								'Date of Birth': ["not available", "n.a."],
# 								'Address': ["not available", "n.a."],
# 								'Age': [-1]
# 								}, skiprows=1)
# print(df)


# # ----------- Writing the dataframe content to csv -------------
# file_path = "../sample_files/new_data.csv"
# df.to_csv(file_path, index=False)

# # ----------- Writing the dataframe content to csv with few columns -------------
# file_path = "../sample_files/new_data_few_columns.csv"
# df.to_csv(file_path, index=False, columns=["Name", "Address"])

# # ----------- Writing the dataframe content to csv with few columns -------------
# file_path = "../sample_files/new_data_without_header.csv"
# df.to_csv(file_path, index=False, header=False)


# # ------------------ Reading excel file and creating dataframe ----------------
# path = "../sample_files/sample_excel.xlsx"
# df = pd.read_excel(path)
# print(df)

# # ------------------ Reading excel file with specifying sheet name and creating dataframe ----------------
# path = "../sample_files/sample_excel.xlsx"
# df = pd.read_excel(path, "Sheet1")
# print(df)


# # ------------------ Reading excel file and creating dataframe. Replace some values by creating a custome fucntion ----------------
# def modify_name_values(value):
# 	if value == "Amit":
# 		return "Aman"
# 	else:
# 		return value

# def modify_age_values(value):
# 	if value == 15:
# 		return 55
# 	else:
# 		return value

# path = "../sample_files/sample_excel.xlsx"
# df = pd.read_excel(path, "Sheet1", converters= {
# 		'Name': modify_name_values,
# 		'Age': modify_age_values
# 	})
# print(df)

# # ----------------- Writing dataframe to excel file ------------------------
# # df.to_excel("../sample_files/new_excel.xlsx", sheet_name="Sheet1", startrow = 2, startcol=2) # 
# df.to_excel("../sample_files/new_excel.xlsx", sheet_name="Sheet1", index=False)

# # ------------------- Writing different dataframe to different sheet in excel file --------------------
# user_df = pd.DataFrame({
# 				'Name': ["Ajay", "Amit", "Vijay", "Tarun", "Yogesh", "Yash"],
# 				'Date of Birth': ["10-04-1991", "15-03-1992", "03-07-1995", "29-10-1997", "21-12-1999", "20-01-2000"],
# 				'Address': ["Bhiwadi", "Ajmer", "Jaipur", "Behror", "Alwar", "Kota"],
# 				'Age': [1, 10, 15, 20, 23, 25] 
# 			  })

# customer_df = pd.DataFrame({
# 				'Name': ["Customer 1", "Customer 2"],
# 				'Address': ["Pune", "Mumbai"],
# 				'Age': [25, 45] 
# 			  })

# with pd.ExcelWriter('../sample_files/user_customer.xlsx') as writer:
# 	user_df.to_excel(writer, sheet_name="user_data", index=False)
# 	customer_df.to_excel(writer, sheet_name="customer_data", index=False)


# ----------------------- Pandas loc function to read data loc[rows, columns] ----------------------------------------------------------

path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print("------------------ Main dataframe -------------------")
print(df)
print()

# columnwise selection

#  Reading all rows and one specific colunm
print("-------- Reading all rows and one specific column using loc ------")
print(df.loc[:,'Name' ])
print()

#  Reading all rows and some specific columns
print("-------- Reading all rows and some specific columns using loc ------")
print(df.loc[:,['Name', 'Address'] ])
print()

# rowwise selection

#  Reading one row and all colunms
print("-------- Reading one row and all colunms using loc ------")
print(df.loc[ 3,: ])
print()

#  Reading some rows and all columns
print("-------- Reading some rows and all columns using loc ------")
print(df.loc[ [3,4], : ])
print()

# Specific cell selection

#  Reading some rows and some columns
print("-------- Reading some rows and some columns using loc ------")
print(df.loc[ [3, 4], ['Name', 'Address'] ])
print()

#  Reading single cell value
print("-------- Reading single cell value using loc ------")
print(df.loc[3, 'Name'])
print()

# Reading single row
print("-------- Reading single row using loc ------")
print(df.loc[3])
print()


# ----------------------- Pandas iloc function to read data iloc[rows, columns] (We use index values instead of row and column names ---------------------------------------------

path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print("------------------ Main dataframe -------------------")
print(df)
print()

# columnwise selection

# Reading all rows and one specific colunm
print("-------- Reading all rows and one specific column using iloc ------")
print(df.iloc[:, 0 ])
print()

#  Reading all rows and some specific columns
print("-------- Reading all rows and some specific columns using iloc ------")
print(df.iloc[:, [0, 1] ])
print()

# rowwise selection

#  Reading one row and all colunms
print("-------- Reading one row and all colunms using iloc ------")
print(df.iloc[ 3,: ])
print()

#  Reading some rows and all columns
print("-------- Reading some rows and all columns using iloc ------")
print(df.iloc[ [3,4], : ])
print()

# Specific cell selection

#  Reading some rows and some columns
print("-------- Reading some rows and some columns using iloc ------")
print(df.iloc[ [3, 4], [0, 1] ])
print()

#  Reading single cell value
print("-------- Reading single cell value using iloc ------")
print(df.iloc[3, 0])
print()

# Reading single row
print("-------- Reading single row using iloc ------")
print(df.iloc[3])
print()

# ----------------------- Pandas at function to read data at[rows, columns]  ---------------------------------------------

path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print("------------------ Main dataframe -------------------")
print(df)
print()

#  Reading single cell value
print("-------- Reading single cell value using at ------")
print(df.at[3, 'Name'])
print()

# ----------------------- Pandas at function to read data iat[rows, columns] (We use column indexes instead of column names)  ---------------------------------------------

path = "../sample_files/sample_excel.xlsx"
df = pd.read_excel(path)
print("------------------ Main dataframe -------------------")
print(df)
print()

#  Reading single cell value
print("-------- Reading single cell value using iat ------")
print(df.iat[3, 0])
print()


# ------------------ Adding columns to dataframe(4 ways of adding columns) ---------------

print("------------  1st way of adding column to exising dataframe -----------------")
df['Education'] = ['10 th', '12 th', 'B.A.', 'B.Sc.', 'B.Com.', 'B.Tech.']
print(df)
df.drop(['Education'], axis=1, inplace=True)
print()

print("------------  adding multiple columns at once to exising dataframe -----------------")
df[ ['col1', 'col2', 'col3'] ] = np.random.randint(10, size=(6,3))
print(df)
df.drop([ 'col1', 'col2', 'col3' ], axis=1, inplace=True)
print()

print("------------  2nd way of adding column to exising dataframe using index(index, column_name, value) -----------------")
df.insert(1, 'col1_ind', ['10 th', '12 th', 'B.A.', 'B.Sc.', 'B.Com.', 'B.Tech.'])
print(df)
df.drop(['col1_ind'], axis=1, inplace=True)
print()

df.insert(1, 'col1_ind', 5)
print(df)
df.drop(['col1_ind'], axis=1, inplace=True)
print()

df.insert( loc=1, column='col1_ind', value=5)
print(df)
df.drop(['col1_ind'], axis=1, inplace=True)
print()


print(("-----------  3rd way of adding column to existing dataframe using df.assign(new_column=lambda x: x.another_column * 3) "))
df = df.assign(Roll_Number = lambda x: x.Age * 4 )
print(df)
df.drop(['Roll_Number'], axis=1, inplace=True)
print()

print(("-----------  4th way of adding column to existing dataframe using loc[:,'column_name'] = [val1, val2, ....] "))
df.loc[:,"Roll_Number"] = [1,2,3,4,5,6]
print(df)
df.drop(['Roll_Number'], axis=1, inplace=True)
print()



