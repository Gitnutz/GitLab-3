import MalevolentNUTZ.bmi as MalevolentNUTZ
def test_bmi_normal_weight():
    result = MalevolentNUTZ.calculate_bmi(1.73, 60)

    assert (result == 0)

def test_bmi_over_weight():
    result = MalevolentNUTZ.calculate_bmi(1.67, 6000)

    assert (result == 1)

def test_bmi_under_weight():
    result = MalevolentNUTZ.calculate_bmi(1.89, 53)

    assert (result == -1)