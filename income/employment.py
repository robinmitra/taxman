class Employment:
    def __init__(self, salary, period='yearly'):
        self._salary = salary if period == 'yearly' else salary * 12

    def get_salary(self, period='yearly'):
        return self._salary if period == 'yearly' else self._salary / 12
