import pandas as pd

# csv
df = pd.read_csv(
        'sample.csv',
        names=["R","N","A","M","C"],
        skiprows=1,
        nrows=5,
        usecols=[1,4]   
    )
# print(df)

# header
# names
# usecols
# skiprows
# nrows

# index_col
# sep = ""
# encoding ="utf-8"

# excel
df = pd.read_excel("sample.xlsx",sheet_name="Products",header=0,nrows=5)
# print(df)

# sheet_name
# header
# usecols
# skiprows
# nrows

# json
df = pd.read_json("sample.json")
# print(df)


# html
# list of df
df = pd.read_html("sample.html") # [df,df,df,df,df]
print(df[0])
print(df[1])