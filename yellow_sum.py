import pandas as pd
from datetime import datetime

df = pd.read_csv('simple_nyc_yellow.csv')

count_pickup = {}
year_2013 = datetime.strptime('01-01-13', '%m-%d-%y').date().year

for index, row in df.iterrows():
    dt = datetime.strptime(row['pickup_datetime'], '%m-%d-%y %H:%M:%S').date()
    if dt.year != year_2013:
        continue
    date = dt.strftime("%m-%d-%y")
    # print(dt)
    c = int(row['passenger_count'])
    # print(c)
    if date in count_pickup:
        count_pickup[date] += c
    else:
        count_pickup[date] = c

#print(count_pickup)

data_lst = []
value_lst = []
for date in count_pickup.keys():
    data_lst.append(date)
    value_lst.append(count_pickup[date])

data = {'Date': data_lst, 'Volumn': value_lst }
df = pd.DataFrame(data)

# def ret(row):
#     return count_pickup[row['Date']]
# df['volumn'] = df.apply(ret, axis=1)
df.to_csv('counts_yellow.csv')




# def ct(row):
#     # 08-25-13 03:04:20
#     dt = datetime.strptime(row['pickup_datetime'], '%m-%d-%y %H:%M:%S').date()
#     print(dt)
#     c = int(row['passenger_count'])
#     print(c)
#     if dt in count_pickup:
#         count_pickup[dt] += c
#     else:
#         count_pickup[dt] = c

#data = {"":}
# count = df.apply(ct, axis=1)

# df = pd.DataFrame(count)
# df.to_csv('counts.csv')



