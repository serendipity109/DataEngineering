import pandas as pd
from dask import dataframe as dd

odd_numbers = list(range(1, 11, 2))
even_numbers = list(range(2, 11, 2))

pandas_df = pd.DataFrame({'odd_num': odd_numbers, 'even_num': even_numbers})

print(pandas_df)

dask_df = dd.from_pandas(pandas_df, npartitions=2)

# Uncomment the line below if you are using Mac
dask_df.to_csv("./activity22.1/", index=False)

# Uncomment the line below if you are using Windows
# df.to_csv("C:/tmp/mo-pcde/activity22.1/", index=False)
