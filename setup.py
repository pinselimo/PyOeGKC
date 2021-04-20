from setuptools import setup
import os

DESC = "Convert municipality codes of Austrian towns throughout time"

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Education",
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt") as f:
    INSTALL_REQUIRES = [r.strip() for r in f.readlines()]

setup(
    name="pyoegkc",
    version="0.0b1",
    description=DESC,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Simon Plakolb",
    author_email="simon.plakolb@uni-graz.at",
    license="MIT",
    platforms="any",
    packages=["pyoegkc"],
    package_dir={"pyoegkc": "pyoegkc"},
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.5",
    classifiers=CLASSIFIERS,
)
