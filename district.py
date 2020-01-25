import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from matplotlib.path import Path
import math

stations = pd.read_csv('nyc_bikeshare_key.csv')
ntas = pd.read_csv('geographic.csv')
nta_shapes = {}

for (colName, colData) in ntas.iteritems():
    coordinates = colData.values
    # coord = np.array([[coordinates[0], coordinates[1]], [coordinates[2], coordinates[3]], [coordinates[4], coordinates[5]]])
    coord = np.array([[coordinates[0], coordinates[1]]])
    i = 2
    while i < len(coordinates):
        if math.isnan(coordinates[i]):
            break
        coord = np.append(coord, np.array([[coordinates[i], coordinates[i+1]]]), axis=0)
        i += 2
    pol = Polygon(coord)
    # pol = Path(coord)
    nta_shapes[colName] = pol

#print(nta_shapes)

def check_points(row):
    lon = row['station_longitude']
    lat = row['station_latitude']
    # poi = np.array([lon, lat])
    # p = Point(poi)
    p = Point(lon, lat)
    for nta in nta_shapes:
        if nta_shapes[nta].contains(p):
            return nta
    return ""

stations["nta_code"] = stations.apply(check_points, axis=1)

stations.to_csv('with_ntas.csv')
