from distutils.core import setup
from setuptools import find_packages

setup(
	name="snowflake",
	version="0.1",
	author="DSSS"
	author_email="harshanaa153@gmail.com"
	packages=find_packages(),
	install_requires=["numpy","turtles","random"]
)