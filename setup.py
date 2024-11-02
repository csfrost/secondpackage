from setuptools import setup, find_packages

setup(
    name= 'secondpackage',
    version= '0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python packages',
    long_description=open('readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/csfrost/secondpackage',
    author='Clarke Shokare',
    author_email='clarke.shokare@gmail.com'
)