import pandas as pd

# csv
df = pd.read_csv('sample.csv')

print(df)
df.to_csv('data.csv',index=False)
df.to_excel('data.xlsx',index=False)
df.to_json('data.json',indent=4,index=False)
df.to_html('data.html',index=False)

