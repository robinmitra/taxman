class Summary:
    def __init__(self, total_income, net_income, income_tax, employees_ni,
                 employers_ni):
        self._total_income = total_income
        self._net_income = net_income
        self._income_tax = income_tax
        self._employees_ni = employees_ni
        self._employers_ni = employers_ni

    @property
    def total_income(self):
        return self._total_income

    @property
    def net_income(self):
        return self._net_income

    @property
    def income_tax(self):
        return self._income_tax

    @property
    def employees_ni(self):
        return self._employees_ni

    @property
    def employers_ni(self):
        return self._employers_ni
