from os.path import abspath, join
from setuptools import setup

_local_dir: str = abspath(__file__)
_readme: str = join(_local_dir, 'README.md')

setup(
    name='diceman',
    version='0.1.1',
    description='Simulates dice rolls for tabletop games',
    long_description=_readme,
    long_description_content_type="text/markdown",
    url='https://github.com/martinak1/diceman',
    author='martinak1',
    author_email='abc000100100011@gmail.com',
    license='BSD-3-Clause',
    packages=['diceman'],
    install_requires=['discord'],
    zip_safe=False
)