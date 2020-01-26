import pandas as pd

df1 = pd.read_csv('../../nyc_bikeshare_key.csv')
df2 = pd.read_csv('../../dataset_heads/dataset_1.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'station_id')
df3.set_index('station_id', inplace = True)

df3.to_csv('CSV3.csv')