from pkg_resources import parse_requirements
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = [str(req) for req in parse_requirements(f)]

setup(
    name="prem",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
)
