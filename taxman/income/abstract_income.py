import abc


class AbstractIncome(abc.ABC):
    @abc.abstractmethod
    def get_amount(self):
        """Get income amount for the income type"""
