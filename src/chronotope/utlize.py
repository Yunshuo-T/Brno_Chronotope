import geopandas as gpd
from shapely import Polygon
import numpy as np

def tessellation(bounds, size,crs):
    xmin, ymin, xmax, ymax = bounds
    grids = []
    for x0 in np.arange(xmin,xmax,size):
        for y0 in np.arange(ymin,ymax,size):
            x1 = x0 + size
            y1 = y0 + size
            cell = Polygon([(x0,y0),(x1,y0),(x1,y1),(x0,y1)])
            grids.append(cell)
    grid = gpd.GeoDataFrame({'grid_id': range(len(grids))}, geometry=grids, crs=crs)
    return grid