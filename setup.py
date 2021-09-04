from setuptools import find_packages, setup
from databricks_cicd_template import __version__

setup(
    name="databricks_cicd_template",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="",
)
