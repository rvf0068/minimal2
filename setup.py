"""Setup file for a minimal package"""

from setuptools import setup

setup(name='minimal',
      version='0.1',
      description='A Python package for something',
      url='http://github.com/rvf0068/minimal',
      author='Yo Mero',
      author_email='yomero@gmail.com',
      license='MIT',
      packages=['minimal'],
      include_package_data = True,
      package_data = {
      '' : ['*.png'],
      '' : ['*.txt'],
      }
      zip_safe=False)


