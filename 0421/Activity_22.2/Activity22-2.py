import dask.dataframe as ddf
from dask import delayed


df = ddf.read_csv("data/2000*.csv", assume_missing=True)

df.compute()

print(df.head())

mean = df['x'].mean().compute()
print(f'mean: {mean}')

cols = len(df.columns)
print(f'columns: {cols}')
