import pandas as pd
from datetime import datetime

df1 = pd.read_csv('counts_yellow.csv')
df2 = pd.read_csv('counts.csv')

count_pickup = {}
year_2013 = datetime.strptime('01-01-13', '%m-%d-%y').date().year

for index, row in df1.iterrows():
    dt = datetime.strptime(row['Date'], '%m-%d-%y').date()
    date = dt.strftime("%Y-%m-%d")
    c = row['Volumn']
    if date in count_pickup:
        count_pickup[date] += c
    else:
        count_pickup[date] = c

for index, row in df2.iterrows():
    dt = datetime.strptime(row['Date'], '%m-%d-%y').date()
    if dt.year != year_2013:
        continue
    date = dt.strftime("%Y-%m-%d")
    c = row['Volumn']
    if date in count_pickup:
        count_pickup[date] += c
    else:
        count_pickup[date] = c

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
df.to_csv('counts_all.csv')