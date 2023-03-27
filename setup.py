import pkg_resources
from setuptools import setup
from setuptools import setup, find_packages


def get_requirements(path):
    with open(path) as f:
        reqlist = [i for i in f.read().splitlines() if not i.startswith(
            '#') and not i.startswith('-')]
    return reqlist


# Check if package is already installed and of the same version or below
try:
    installed_version = pkg_resources.get_distribution("mypackage").version
    if pkg_resources.parse_version(installed_version) >= pkg_resources.parse_version("1.0.0"):
        print("mypackage is already installed and of the same version or below")
    else:
        print("mypackage is installed but not of the same version or below, installing with -e .")
        setup(name='mypackage', packages=['mypackage'], install_requires=[
        ], extras_require={}, dependency_links=['-e .'])
except pkg_resources.DistributionNotFound:
    print("mypackage is not installed, installing with -e .")
    setup(name='genericmlboilerplate',
          version='0.1',
          packages=find_packages(),
          install_requires=get_requirements('requirements.txt'),
          # metadata for upload to PyPI
          author="Sagar Yadav",
          author_email="sagar@sagaryadav.com",
          description="Fast ML model develoment boilerplate",
          license="PSF",
          keywords="machine learning boilerplate data science",
          dependency_links=['-e .']
          )
