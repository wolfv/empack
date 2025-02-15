#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["typer", "requests", "pydantic"]

setup(
    author="Thorsten Beier",
    author_email="derthorstenbeier@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="empack emscripten+boa",
    entry_points={
        "console_scripts": [
            "empack=empack.cli.main:app",
        ],
    },
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="empack",
    name="empack",
    packages=find_packages(),
    url="https://github.com/emscripten-forge/empack",
    version="0.8.0",
    zip_safe=False,
)
