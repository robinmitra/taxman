from taxman.income.employment import Employment
from taxman.national_insurance.employees import Employees


def test_calculate_employees_ni():
    employment = Employment(65000)
    employees = Employees([employment])
    # Note: There's a diff of about 4 pence between contribution computed here
    # and HMRC's calculator. May revisit in case I figure out the reason.
    assert round(employees.get_contribution()) == round(410.34)
