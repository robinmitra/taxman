from taxman.income.employment import Employment


class Employees:
    def __init__(self, incomes):
        self._incomes = incomes

    def get_contribution(self):
        """ Calculate Class 1 Employee's NIC.

        Returns:
           float: The total contribution.
        """
        salary = self._get_salary()
        if not salary:
            return 0
        # Class 1 NIC
        contribution = 0
        pt, uel = 702, 3863
        if salary > uel:
            contribution = (salary - uel) * 0.02 + (uel - pt) * 0.12
        elif salary > pt:
            contribution = (salary - pt) * 0.12
        return contribution

    def _get_salary(self):
        employment = next(
            income for income in self._incomes if type(income) is Employment)
        return employment.get_salary('monthly')
