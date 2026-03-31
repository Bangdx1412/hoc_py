import pandas as pd

df = pd.read_csv("pandas/ds.txt",sep=',',header=None,names=['ma','ten','lop','quequan'])
print(df)