from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="amk_testhelpers",
    version="0.0.1",
    author="Markku Viertokangas",
    author_email="markku.viertokangas@hotmail.com",
    description="Contains helper functions for unit testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={'': ['python/allowed_libraries.txt']},
    license="MIT",
    entry_points={
        "console_scripts": [
            "test_assignment=amk_testhelpers.execute_test:runTest",
            "allowed_libraries=amk_testhelpers.python.get_libraries:print_allowed_libraries",

        ]
    },
    url="https://github.com/Markvi268/amk_testhelpers",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        
    ],

    python_requires=">=3.10",

)