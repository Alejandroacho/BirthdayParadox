import cumple
import math

def test_median_is_fine():
    iterations = 10000
    number_of_people = 10000
    expected_value = 23
    actual_value = cumple.calculate_median(iterations, number_of_people)
    assert expected_value == math.floor(actual_value)