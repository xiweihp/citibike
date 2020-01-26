import pandas as pd
from datetime import datetime
import numpy as np
import math

df = pd.read_csv('nyc_bikeshare.csv')
# df = pd.read_csv('../../dataset_heads/dataset_1.csv')
df2 = pd.read_csv('legend/nyc_bikeshare_key.csv')

arr = []
df2.set_index('station_id', inplace=True)
# df2 = df2.reindex(index='station_id', columns=['station_latitude', 'station_longitude'])

def find_station_lat(stid):
    return df2.loc[stid]['station_latitude']

def find_station_log(stid):
    return df2.loc[stid]['station_longitude']

for index, row in df.iterrows():
    r = ['Origin']
    s = row['start_station_id']
    if math.isnan(s):
        continue
    r.append(s)
    r.append(index)
    r.append(find_station_lat(s))
    r.append(find_station_log(s))

    r2 = ['Destination']
    e = row['end_station_id']
    if math.isnan(e):
        continue
    r2.append(e)
    r2.append(index)
    r2.append(find_station_lat(e))
    r2.append(find_station_log(e))
    arr.append(r)
    arr.append(r2)

data = np.array(arr)
output = pd.DataFrame({'Origin-Destination': data[:, 0], 'Station': data[:, 1], 'Path_ID': data[:, 2],'Latitude': data[:, 3], 'Longitude':data[:, 4]})
# output = pd.DataFrame(data=arr[0:,0:], columns=['Origin-Destination','Station','Path_ID','Latitude', 'Longitude'])
output.to_csv('test1.csv')