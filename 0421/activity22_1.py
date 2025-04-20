import pandas as pd
from dask import dataframe as dd

#create pandas dataframe


#set npartition argument
df = dd.from_pandas(pandas_df)

#Uncomment the line below if you are using Mac
#df.to_csv("./activity22.1/", index=False)

#Uncomment the line below if you are using Windows
#df.to_csv("C:/tmp/mo-pcde/activity22.1/", index=False)