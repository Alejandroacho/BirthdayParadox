import math
import pytest

from calculate_median import calculate_median, calculate_number_of_people


def test_median_is_fine():
    iterations = 10000
    number_of_people = 10000
    expected_value = 23
    actual_value = calculate_median(iterations, number_of_people)
    assert expected_value == math.floor(actual_value)

def test_raise_value_error_when_small_sample_is_passed_to_people_calculator():
    with pytest.raises(ValueError):
        calculate_number_of_people(2)

def test_raise_type_error_when_no_int_passed_to_people_calculator():
    with pytest.raises(TypeError):
        calculate_number_of_people("test")

def test_raise_type_error_when_no_int_passed_to_median_calculator():
    with pytest.raises(TypeError):
        calculate_median(2, "test")
        calculate_median("test", 2)