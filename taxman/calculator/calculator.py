from functools import reduce

from taxman.calculator.summary import Summary
from taxman.national_insurance.employees import Employees
from taxman.national_insurance.employers import Employers
from taxman.tax.income_tax import IncomeTax


class Calculator:
    def __init__(self, incomes, allowances):
        self._incomes = incomes
        self._allowances = allowances
        self._tax = 0

    def calculate(self):
        tax_amount = IncomeTax(self._incomes, self._allowances).calculate()
        employees_ni = Employees(self._incomes).get_contribution()
        employers_ni = Employers(self._incomes).get_contribution()
        income_amounts = [income.get_amount() for income in self._incomes]
        total_income = reduce(
            lambda total, income: total + income, income_amounts)
        net_income = total_income - (tax_amount + employees_ni)
        return Summary(
            total_income, net_income, tax_amount, employees_ni, employers_ni)
