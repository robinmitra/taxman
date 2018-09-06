from allowance.personal_allowance import PersonalAllowance
from income.employment import Employment
from tax.income_tax import IncomeTax


class Calculator:
    def __init__(self, incomes, allowances):
        self._incomes = incomes
        self._allowances = allowances
        self._tax = 0

    def calculate(self):
        tax_amount = IncomeTax(self._incomes, self._allowances).calculate()
        return tax_amount


allowance = PersonalAllowance(11850)
employment = Employment(65000)

calculator = Calculator([employment], [allowance])
tax = calculator.calculate()
print('Tax: {}'.format(tax))
