import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="cdfgeonode",
    version="0.2",
    author="",
    author_email="",
    description="cdfgeonode, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="cdfgeonode geonode django",
    url='https://github.com/cdfgeonode/cdfgeonode',
    packages=['cdfgeonode',],
    include_package_data=True,
    zip_safe=False,
)
