import pandas as pd

theID = [1,0,1,0,0,0,0,0,1,1,1]
x = [0.5]*len(theID)
y = [0.2]*len(theID)

df = pd.DataFrame({'id': theID,
                   'x': x,
                   'y': y})
print(df)
df.to_csv("/Users/evan/Desktop/The-ML-book/name.csv", index=False, header=True)

df1 = pd.read_csv("name.csv")
x = df1['x'].tolist()
y = df1['y'].tolist()
print(x)
print(y)

import os
os.system('rm name.csv')