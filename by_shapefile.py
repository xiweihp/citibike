import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import shape
import shapefile


stations = pd.read_csv('dataset_1_key.csv')
shp = shapefile.Reader('nynta.shp') #open the shapefile
all_shapes = shp.shapes() # get all the polygons
nta_shapes = dict()

for i in range(len(all_shapes)):
    boundary = all_shapes[i] # get a boundary polygon
    nta_shapes[colName] = Polygon(coord)

def check_points(row):
    lon = row['station_longitude']
    lat = row['station_latitude']
    p = Point(lon, lat)

    # for i in range(len(all_shapes)):
    #     boundary = all_shapes[i] # get a boundary polygon
    #     if Point(p).within(shape(boundary)): # make a point and see if it's in the polygon
    #        print ("The point is in")

stations.apply(check_points, axis=1)