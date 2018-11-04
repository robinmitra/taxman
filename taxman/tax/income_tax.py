from taxman.allowance.personal_allowance import PersonalAllowance
from taxman.income.employment import Employment


class IncomeTax:
    def __init__(self, incomes, allowances):
        self._incomes = incomes
        self._allowances = allowances

    def calculate(self):
        employment_income = next(
            income for income in self._incomes if type(income) is Employment)
        tax_free, basic_rate, higher_rate, additional_rate = self.get_bands(
            employment_income.get_salary())
        tax = (basic_rate * 0.2) + (higher_rate * 0.4) + (
            additional_rate * 0.45)
        return tax

    def get_bands(self, income):
        personal_allowance = next(
            allowance for allowance in self._allowances
            if type(allowance) is PersonalAllowance)
        pa = personal_allowance.get_allowance()
        basic_rate_end, higher_rate_end = 46350, 150000
        tax_free = pa if income > pa else income
        basic_rate, higher_rate, additional_rate = 0, 0, 0
        if income > pa:
            basic_rate = basic_rate_end - pa
            if income > higher_rate_end:
                higher_rate = higher_rate_end - basic_rate_end
                additional_rate = income - higher_rate_end
            elif income > basic_rate_end:
                higher_rate = income - basic_rate_end
        return tax_free, basic_rate, higher_rate, additional_rate
