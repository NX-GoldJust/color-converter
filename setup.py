from setuptools import setup, find_packages
__version__ = "0.0.1"
import pathlib
setup(
    name="colorconverter",
    version=__version__,
    install_requires=[],
    description="Color converter",
    author="GoldJust",
    python_requires=">=3.11",
    packages=find_packages(),
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/GoldJust/color-converter/issues",
        "Source Code": "https://github.com/GoldJust/color-converter",
    },
    include_package_data=True
)