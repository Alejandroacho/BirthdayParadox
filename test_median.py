from calculate_median import calculate_median, calculate_number_of_people
import math

def test_median_is_fine():
    iterations = 10000
    number_of_people = 10000
    expected_value = 23
    actual_value = calculate_median(iterations, number_of_people)
    assert expected_value == math.floor(actual_value)