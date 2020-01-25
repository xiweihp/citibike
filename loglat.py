import pandas as pd
import math

ntas = pd.read_csv('geographic.csv')

for (colName, colData) in ntas.iteritems():
    coordinates = colData.values
    # coord = np.array([[coordinates[0], coordinates[1]], [coordinates[2], coordinates[3]], [coordinates[4], coordinates[5]]])
    coord_log = [coordinates[0]]
    coord_lat = [coordinates[1]]
    i = 2
    while i < len(coordinates):
        if math.isnan(coordinates[i]):
            break
        coord_log.append(coordinates[i])
        coord_lat.append(coordinates[i+1])
        i += 2
    lat_name = colName + "_lat"
    log_name = colName + "_log"
    ntas[lat_name] = coord_lat
    ntas[log_name] = coord_log

ntas.to_csv("loglat.csv")