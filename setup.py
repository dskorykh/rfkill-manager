from setuptools import setup, find_packages

setup(
    name='rfkill_manager',
    version='1.0.0',
    author='Dmitry Skorykh',
    author_email='dmitry.skorykh@emlid.com',
    packages=find_packages(exclude=['tests']),
    description='Python API to manage rfkill',
    long_description=open('README.md').read(),
)
