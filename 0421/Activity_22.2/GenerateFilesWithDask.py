import dask 
import os
import datetime
if not os.path.exists('data'):
    os.mkdir('data')
def name(i):
    return str(datetime.date(2000,1,1) + i * datetime.timedelta(days=1))

df = dask.datasets.timeseries()
df.to_csv('data/*.csv', name_function=name)