import pandas as pd

df = pd.read_excel("sample.xlsx",sheet_name="branch")
result = df["Name"]
result = df[["Name","Marks"]]
# slicing
result = df[2:5]

# location i.e loc
result = df.loc[1,"Name"]
result = df.loc[0:1,["Name","Marks"]]
result = df.loc[:,["Name","Marks"]]

# iloc
result = df.iloc[0:4,1:4]
result = df.iloc[:,1:4]

# at => single
result = df.at[0,"Name"]
# at => single
result = df.iat[0,1]



print(result)