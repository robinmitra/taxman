from distutils.core import setup

setup(
    name='taxman',
    version='0.1.0',
    packages=['taxman', 'taxman.allowance', 'taxman.calculator', 'taxman.income',
              'taxman.national_insurance', 'taxman.person', 'taxman.tax'],
    scripts=['bin/taxman'],

    # Metadata
    author='Robin Mitra',
    author_email='robinmitra1@gmail.com',
    description='Tax calculator',
    url='https://github.com/robinmitra/taxman',
    license='MIT',
    keywords='tax, calculator'
)
