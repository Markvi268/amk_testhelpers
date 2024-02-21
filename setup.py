from setuptools import setup, find_packages

setup(
    name="test_package",
    version="0.0.1",
    author="Markku Viertokangas",
    author_email="markku.viertokangas@hotmail.com",
    description="Contains helper functions for unit testing",
    long_description="test_package is a package that contains auxiliary functions for unit testing, including the runTest() method, which receives tests.py module.",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        
    ],

    python_requires=">=3.6",

)