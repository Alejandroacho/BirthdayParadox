import random

YEAR_DAYS = 365

def calculate_number_of_people(number_of_people):
    birthdays = []
    if type(number_of_people) != int:
        raise TypeError("number_of_people must be an integer")
    for person_number in range(number_of_people):
        person_birthday = random.randint(1, YEAR_DAYS)
        if person_birthday not in birthdays:
            birthdays.append(person_birthday)
        elif person_birthday in birthdays:
            return person_number
    raise ValueError("Can't find person number maybe due to a small statistic sample")

def calculate_median(iterations, number_of_people):
    if type(iterations) != int or type(number_of_people) != int:
        raise TypeError("number_of_people must be an integer")
    sum_of_numbers_given = sum(calculate_number_of_people(number_of_people) \
                               for _ in range(iterations))
    median = sum_of_numbers_given / iterations
    return median

median = calculate_median(10000, 10000)
print(f"Median is: {median}")
