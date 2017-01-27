"""proximity: calculate distances from raster features"""

import logging

__author__ = "Matthew Parker"
__version__ = '1.0.0'

# Get a logger object using the name of this module. Do not however
# configure this or Python's root logger: the `rio` program, of which
# this is a subcommand, makes the necessary configuration.
logger = logging.getLogger(__name__)
