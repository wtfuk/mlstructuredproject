from setuptools import setup, find_packages


def get_requirements(path):
    with open(path) as f:
        reqlist = [i for i in f.read().splitlines() if not i.startswith('#') and not i.startswith('-')]
    return reqlist


setup(
    name = "genericmlboilerplate",
    version="0.1",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
    # metadata for upload to PyPI
    author = "Sagar Yadav",
    author_email = "sagar@sagaryadav.com",
    description = "Fast ML model develoment boilerplate",
    license = "PSF",
    keywords = "machine learning boilerplate data science",
)