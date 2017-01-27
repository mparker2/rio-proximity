from codecs import open as codecs_open
from setuptools import setup, find_packages

# Parse the version from the fiona module.
with open('proximity/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='rio-proximity',
      version=version,
      description=u"Calculate distances from raster features",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Matt Parker",
      author_email='mparker2@sheffield.ac.uk',
      url='https://github.com/mparker2/rio-proximity',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'scipy',
          'rasterio'
      ],
      entry_points="""
      [rasterio.rio_commands]
      proximity=proximity.scripts.proximity:proximity
      """)
