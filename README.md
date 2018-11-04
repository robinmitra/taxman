Tax Tools
=========

Taxman provides a set of tools for computing Income Tax and National Insurance 
contributions for the UK tax system.

It currently supports calculating Income Tax and National Insurance 
contributions (for both employer and employee), and deducting these to return 
the net income. 

At the moment, it can only calculate these for the tax year 2018-19, but 
support for configuring it to calculate for any tax year will be added soon.

Requirements
------------

The current version of Taxman has been tested to work on Python 3.6. 
Although it may work on other versions, it is recommended to use this version 
in case you encounter any problems.

Installation
------------

The easiest way to install Taxman is to use pip:

```bash
pip install taxman
```

Building from source
--------------------

If you wish to build and install Taxman from source, following these steps:

1. Clone the repository:

```bash
git clone git@github.com:robinmitra/taxman.git
```

2. Install Pipenv if it isn't already, as this project uses it to help manage 
dependencies. Once you have Pipenv, install all dependencies (including dev):

```bash
pipenv install --dev
```

3. Activate the virtual environment created by Pipenv:

```bash
pipenv shell
```

4. Run tests to ensure everything is setup correctly:

```bash
make test
```

5. Install the package:

```bash
python setup.py install
```

Usage
-----

Run the following to print Income Tax and National Insurance contributions, 
along with the net income, for a given salary and personal allowance: 

```bash
taxman --employment-income 85000 --personal-allowance 11850
```