# Generate the distance matrix

## Get list of the grids within the defined distance from each grid

The full scripts is saved in `get_grids_within_distance.py`. The script is run as follows:

It requires the following libraries:

1. GeoPandas
2. Shapely

The input files are in the format of geojson.

In this example, I am using a grid.shp file. Therefore, it contains an extra step to extract the centroids of the grids. If your data is in the format of centroids, you can skip this step.

The script will add three columns to the original grid.shp file:

- 'list_ids_4h': The list of IDs of the grids within 400 meters from the grid
- 'list_ids_1k': The list of IDs of the grids within 1 kilometre from the grid
- 'list_ids_25h': The list of IDs of the grids within 2.5 kilometres from the grid

The derived outputs include the following files:

- grid_centroids.geojson: The centroids of the grids with the three columns added
- grids_new.geojson: The grids with the three columns added