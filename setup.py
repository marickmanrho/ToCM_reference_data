# Setup for the ToCM reference data package
#
# Written using https://packaging.python.org/tutorials/packaging-projects/

# Most importandly import setuptools
from setuptools import setup
import os

# Use README.md as long description
with open("README.md", "r") as file:
    long_description = file.read()

# Use requirements.txt as requirements
with open("requirements.txt", "r") as file:
    requirements = file.read()

package_location = "tocm_reference_data"
data_files = []
for root, dirs, files in os.walk(package_location + "/lib"):
    for file in files:
        if file.endswith(".json") or file.endswith(".csv"):
            data_files.append(
                os.path.relpath(os.path.join(root, file), package_location)
            )

setup(
    name="tocm_reference_data",
    version=0.4,
    url="https://github.com/marickmanrho/tocm_reference_data",
    license="MIT",
    author="Marick Manrho",
    author_email="marickmanrho@gmail.com",
    description="Reference data used in my research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["scientific", "University of Groningen"],
    install_requires=requirements,
    packages=["tocm_reference_data"],
    entry_points={
        "console_scripts": ["tocm_reference_data=tocm_reference_data.manage:manage"]
    },
    include_package_data=True,
    package_data={"": data_files},
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
