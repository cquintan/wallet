from setuptools import setup, find_packages

with open('README.md') as file:
    readme = file.read()

with open('LICENSE') as file:
    license = file.read()

setup(
    name='wallet',
    version='0.1.0',
    description='Package for wallet',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('main', 'tests', 'docs'))
)