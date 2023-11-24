import geopandas as gpd
from shapely.geometry import Polygon
import os

def get_grids_within_distance(grid, distance):
    """
    This function takes a grid and a distance threshold as input, and returns a list of grid IDs that are within the distance threshold of each grid.
    """
    # generate the gpd of centroids of the grid
    centroids = grid.copy()
    centroids.geometry = centroids.geometry.centroid
    # create a buffer of dist around the centroids
    buffer = centroids.copy()
    for dist in distances:
        buffer.geometry = buffer.geometry.buffer(dist)
        # get the IDs of buffer that intersects with the centroids
        centroids['list_ids_'+str(dist)] = centroids.geometry.apply(lambda x: buffer[x.intersects(buffer.geometry)].OBJECTID.tolist())
        # change the list to string
        centroids['list_ids_'+str(dist)] = centroids['list_ids_'+str(dist)].apply(lambda x: str(x).strip('[]'))
    centroids_df = centroids[['OBJECTID', 'list_ids_400', 'list_ids_1000', 'list_ids_2500']]
    grid = grid.merge(centroids_df, on='OBJECTID', how='left')
    return grid, centroids

if __name__ == "__main__":

    # set up the working directory
    os.chdir('open_codes/spatial-analysis/') # replace with your own working directory

    distances = [400, 1000, 2500] # define the distance thresholds here

    """ change the input file here """
    grid = gpd.read_file("data/get_grids_within_distance/grid.geojson")

    # check the meta data of the grid
    # print(grid.info())

    # check the crs of the grid
    # print(grid.crs)
    grid, centroids = get_grids_within_distance(grid, distances)
    # join back the centroids to the grid
    
    # rename the columns, this step is optional
    grid['list_ids_4h'] = grid['list_ids_400']
    grid['list_ids_1k'] = grid['list_ids_1000']
    grid['list_ids_25h'] = grid['list_ids_2500']
    grid.drop(columns=['list_ids_400', 'list_ids_1000', 'list_ids_2500'], inplace=True)

    centroids.to_file("data/get_grids_within_distance/processed/grid_centroids.geojson", driver='GeoJSON')

    grid.to_file("data/get_grids_within_distance/processed/grid_new.geojson", driver='GeoJSON')
