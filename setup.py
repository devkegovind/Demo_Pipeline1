from setuptools import setup, find_packages
setup(name = 'census-income',
      version = '0.0.1',
      author = 'govind',
      author_email = 'gvdevke@gmail.com',
      package = find_packages(),
      install_requires = ['pandas', 'numpy', 'flask']
      )