from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='taxman',
    version='0.2.0',
    packages=['taxman', 'taxman.allowance', 'taxman.calculator',
              'taxman.income', 'taxman.national_insurance', 'taxman.person',
              'taxman.tax'],
    scripts=['bin/taxman'],

    # Metadata
    author='Robin Mitra',
    description='A set of tools for computing Income Tax and National '
                'Insurance contributions for the UK tax system.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/robinmitra/taxman',
    license='MIT',
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
