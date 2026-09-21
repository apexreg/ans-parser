from setuptools import setup, find_packages

setup(
    name="apexreg-ans-parser",
    version="0.1.0",
    description="Agent Name Service URI parser for ApexRegistry",
    python_requires=">=3.9",
    packages=find_packages(include=["apexreg_ans_parser*"]),
)
