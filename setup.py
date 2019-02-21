from distutils.core import setup

from taxman import __author__, __description__, __license__, __name__, \
    __version__

with open('README.md') as f:
    long_description = f.read()

setup(
    name=__name__,
    version=__version__,
    packages=['taxman', 'taxman.allowance', 'taxman.calculator',
              'taxman.income', 'taxman.national_insurance', 'taxman.person',
              'taxman.tax'],
    scripts=['bin/taxman'],

    # Metadata
    author=__author__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/robinmitra/taxman',
    license=__license__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Office/Business :: Financial :: Accounting',
    ],
    keywords='tax ni calculator taxman uk',
)
