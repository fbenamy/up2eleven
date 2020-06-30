from setuptools import setup

setup(name='up2eleven',
      version='0.1',
      description='A python package for easily creating datasets about music.',
      url='http://github.com/fbenamy/up2eleven',
      author='Faith Benamy',
      author_email='faith.benamy@gmail.com',
      license='MIT',
      packages=['up2eleven'],
      install_requires=['spotipy>=2.13.0',],
      zip_safe=False)