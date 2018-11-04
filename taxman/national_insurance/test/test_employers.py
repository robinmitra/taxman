from taxman.national_insurance.employers import Employers
from taxman.income import Employment


def test_calculate_employees_ni():
    employment = Employment(65000)
    employers = Employers([employment])
    assert round(employers.get_contribution()) == round(650.62)
