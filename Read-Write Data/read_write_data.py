import numpy as np 
import pandas as pd 


# ----------------- Reading csv file with header ------------------

path = "../sample_files/data.csv"
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







