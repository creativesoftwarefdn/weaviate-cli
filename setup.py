from setuptools import setup
from builtins import open

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="weaviate-cli",
      version="0.1.0rc0", # 0.1.0rc0
      description="Comand line interface to interact with weaviate",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="SeMI Technologies",
      author_email="hello@semi.technology",
      packages=["semi", "semi.config", "semi.commands"],
      python_requires='>=2.7',
      install_requires=[
          "weaviate-client==1.2.0",
          "click==7.1.2"]),
