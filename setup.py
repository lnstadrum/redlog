from setuptools import setup
import os

# grab readme
with open(os.path.join("README.md"), "r") as file:
    long_description = file.read()

# build package
setup(
    name="redlog",
    version="0.9",
    author="lnstadrum",
    author_email="",
    description="Python logger to Redis database with threading support",
    install_requires=["redis", "termcolor"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lnstadrum/redlog",
    packages=[""],
    package_data={"": [
        "redlog/__init__.py",
        "redlog/__main__.py",
    ]},
    include_package_data=True
)
