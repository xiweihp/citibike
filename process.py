import pandas as pd

df = pd.read_csv('nyc_green_taxi.csv')
df = df[['pickup_datetime','passenger_count']]

df.to_csv('simple_nyc_green.csv')