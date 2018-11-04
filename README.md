Tax Tools
=========

Taxman provides a set of tools for computing Income Tax and National Insurance 
contributions for the UK.

It currently supports computing Income Tax and National Insurance contributions 
(for both employer and employee), and deducting these to return the net income. 
It can only calculate these for the tax year 2018-19, but will be extended to 
make it easy to support any tax year in future. 

Requirements
------------

The current version of 'taxman' has been tested to work on Python 3.6, 
although it may work on other versions without any issues. Therefore, it is 
recommended to use this version in case you encounter any problems.

Installation
------------

The easiest way to install 'taxman' is to use pip:
`pip install taxman`

Building from source
--------------------

Following the following steps in order to build 'taxman':

1. Clone the repository:

`git clone git@github.com:robinmitra/taxman.git`

2. Install Pipenv if it isn't already, as this project uses it to help manage 
dependencies. Once you have Pipenv, install all dependencies (including dev):

`pipenv install --dev`

3. Activate the virtual environment created by Pipenv:

`pipenv shell`

4. Run tests to ensure everything is setup correctly:

`make test`

5. Install the package:

`python setup.py install`

Usage
-----

Run the following to print Income Tax and National Insurance contributions, 
along with the net income, for a given salary and personal allowance: 

`taxman --employment-income 85000 --personal-allowance 11850`