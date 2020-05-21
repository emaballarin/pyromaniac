# Copyright (c) 2019- Yana Hasson <yana.hasson.inria@gmail.com>
# Copyright (c) 2020- AI-CPS@UniTS
# Copyright (c) 2020- Emanuele Ballarin <emanuele@ballarin.cc>
# SPDX-License-Identifier: Apache-2.0

from setuptools import find_packages, setup
import warnings


DEPENDENCY_PACKAGE_NAMES = ["torch", "pyro"]


def check_dependencies():
    missing_dependencies = []
    for package_name in DEPENDENCY_PACKAGE_NAMES:
        try:
            __import__(package_name)
        except ImportError:
            missing_dependencies.append(package_name)

    if missing_dependencies:
        warnings.warn("Missing dependencies: {}.".format(missing_dependencies))


with open("README.md", "r") as fh:
    long_description = fh.read()


check_dependencies()


setup(
    name="pyromaniac",
    version="0.0.1",
    author="Emanuele Ballarin",
    author_email="emanuele@ballarin.cc",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.7.0",
    description="Collection of PyTorch uses and abuses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emaballarin/pyromaniac",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Linux",
    ],
)
