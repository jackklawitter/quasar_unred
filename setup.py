from setuptools import setup, find_packages


setup(
    name='quasar_unred',
    version='0.1',
    license='MIT',
    author="John Klawitter",
    author_email='jackklawitter@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jackklawitter/quasar_unred',
    keywords='Red Quasars',
    install_requires=[
          'numpy', 'scipy', 'astropy', 'dust_extinction'
      ],

)
