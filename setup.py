# Setup for the ToCM reference data package
#
# Written using https://packaging.python.org/tutorials/packaging-projects/

# Most importandly import setuptools
from setuptools import setup

# Import the main package
import tocm_reference_data

# Use README.md as long description
with open("README.md", "r") as file:
    long_description = file.read()

# Use requirements.txt as requirements
with open("requirements.txt", "r") as file:
    requirements = file.read()

setup(
    name="tocm_reference_data",
    version=tocm_reference_data.__version__,
    url="https://github.com/marickmanrho/tocm_reference_data",
    license="MIT",
    author="Marick Manrho",
    author_email="m.manrho@rug.nl",
    description="Reference data used in my research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["scientific", "University of Groningen"],
    install_requires=requirements,
    packages=["tocm_reference_data"],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
