import random

YEAR_DAYS = 365

def calculate_number_of_persons(number_of_people):
    birthdays = []
    for person_number in range(number_of_people):
        person_birthday = random.randint(1, YEAR_DAYS)
        if person_birthday not in birthdays:
            birthdays.append(person_birthday)
        elif person_birthday in birthdays:
            return person_number

def calculate_median(iterations, number_of_people):
    numbers_given = []
    for _ in range(iterations):
        iteration_number = calculate_number_of_persons(number_of_people)
        numbers_given.append(iteration_number)
    sum_of_numbers_given = sum(number for number in numbers_given)
    median = sum_of_numbers_given / iterations
    return median

median = calculate_median(10000, 10000)
print(f"Median is: {median}")
