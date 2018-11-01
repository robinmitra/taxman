from allowance.personal_allowance import PersonalAllowance
from income.employment import Employment
from tax.income_tax import IncomeTax
from national_insurance.employees import Employees


class Calculator:
    def __init__(self, incomes, allowances):
        self._incomes = incomes
        self._allowances = allowances
        self._tax = 0

    def calculate(self):
        tax_amount = IncomeTax(self._incomes, self._allowances).calculate()
        employees_ni = Employees(self._incomes).get_contribution()
        return tax_amount, employees_ni


allowance = PersonalAllowance(11850)
employment = Employment(65000)

calculator = Calculator([employment], [allowance])
tax, ni = calculator.calculate()
print('Tax: {}'.format(tax))
print('Employees NI: {}'.format(ni))
