from setuptools import setup
import re

version = '1.0.1a'

setup(name='toml-db',
      author='multi-yt76',
      url='https://github.com/multi-yt76/toml-db',
      version=version,
      packages=['tomldb'],
      license='MIT',
      description='A module which acts as a no-sql db, used to easily store and access data in toml format',
      install_requires=['toml>=0.10.2'],
      python_requires='>=3.5.3'
)
