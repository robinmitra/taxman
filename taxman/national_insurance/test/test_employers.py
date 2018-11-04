from taxman.income.employment import Employment
from taxman.national_insurance.employers import Employers


def test_calculate_employees_ni():
    employment = Employment(65000)
    employers = Employers([employment])
    assert round(employers.get_contribution()) == round(650.62)
