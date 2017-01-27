'''
Rasterio Proximity Plugin: produces a raster of distances to features in input
raster layer.

Author: Matthew Parker
Date: 27/01/2017

'''

import numpy as np
import rasterio
from scipy.ndimage import distance_transform_edt
import click

SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=SETTINGS)
@click.argument('input-raster', required=True)
@click.argument('output-raster', required=True)
@click.option('--band', default=1, help='band to process')
@click.option('--data-val', default=255, type=int,
              help='pixel value to calculate distance from')
@click.option('--max-distance', default=None, type=int,
              help='threshold for max distance from features')
@click.option('--dist-geo/--no-dist-geo', default=False,
              help=('Use transform from input raster to convert pixel '
                    'to geo distance'))
def proximity(input_raster, output_raster, band,
              data_val, max_distance, dist_geo):
    with rasterio.open(input_raster) as iraster:
        metadata = iraster.meta.copy()
        transform = iraster.transform
        img = iraster.read(band)
    
    if dist_geo:
        sampling = np.abs([transform[0], transform[4]])
    else:
        sampling = [1, 1]
    distance = distance_transform_edt(img != data_val, sampling=sampling)
    
    if max_distance is not None:
        distance[distance > max_distance] = max_distance
    
    distance = distance.astype(np.float32)
    metadata.update(dtype=rasterio.float32,
                    count=1,
                    compress='lzw',
                    nodata=-999) # zero is meaningful in these rasters
    with rasterio.open(output_raster, 'w', **metadata) as oraster:
        oraster.write(distance, indexes=1)

if __name__ == '__main__':
    proximity()