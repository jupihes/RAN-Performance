# converting excel with few columns into one column 

import pandas as pd
df = pd.read_excel(file_name,sheet_name='Site list')
df['All'] = df[df.columns[1:]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
df = df[['All']]
df = df.All.str.split(',', expand=True)
df = df.T
dff = pd.DataFrame()

for i in np.arange(df.shape[1]-1,0,-1):
     dff = pd.concat([dff, df[df.columns[i]].dropna()], ignore_index=True) #append

dff.columns = ['SITEID']
dff.SITEID.value_counts()
dff.drop_duplicates(keep='first', inplace=True)
