# Copyright (c) 2022 NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

from setuptools import find_packages, setup

packages = find_packages(where="dflex")
packages += find_packages(exclude=["envs*", "examples*"]) + ["dflex.envs", "dflex.examples"]
package_dir = {"": "dflex", "dflex.envs": "envs", "dflex.examples": "examples"}

setup(
    name="dflex",
    version="0.0.1",
    author="NVIDIA",
    author_email="mmacklin@nvidia.com",
    description="Differentiable Multiphysics for Python",
    long_description="",
    long_description_content_type="text/markdown",
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=["ninja", "torch", "numpy", "urchin", "usd-core"],
)
