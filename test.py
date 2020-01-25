import pandas as pd

df = pd.read_csv('simple_nyc_green.csv')
df = df[['pickup_datetime','passenger_count']]

df.head().to_csv('test.csv')