from setuptools import setup
from setuptools import find_packages
from colorconverter import __version__

setup(
    name="colorconverter",
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    description="Color converter",
    author="GoldJust"
)