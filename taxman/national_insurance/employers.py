from taxman.income.employment import Employment


class Employers:
    def __init__(self, incomes):
        self._incomes = incomes

    def get_contribution(self):
        """ Calculate Class 1 Employer's NIC.

        Returns:
            float: The total contribution.
        """
        salary = self._get_salary()
        if not salary:
            return 0
        # Class 1 NIC.
        contribution = 0
        st = 702
        if salary > st:
            contribution = (salary - st) * 0.138
        return contribution

    def _get_salary(self):
        employment = next(
            income for income in self._incomes if type(income) is Employment)
        return employment.get_salary('monthly')
