import random

def calculate_number_of_persons():
    number_of_persons = 20000
    days = 365
    birthdays = []
    has_reached = False
    while not has_reached:
        for person_number in range(number_of_persons):
            person_birthday = random.randint(1, days)
            if person_birthday in birthdays:
                print(f"Birthday already exists: {person_number}")
                has_reached = True
                return person_number
            elif person_birthday not in birthdays:
                birthdays.append(person_birthday)

def calculate_median():
    numbers_calculated = []
    pre_median = 0
    for _ in range(10000):
        iteration_number = calculate_number_of_persons()
        numbers_calculated.append(iteration_number)
    for number in numbers_calculated:
        pre_median = pre_median + int(number)
    return sum(numbers_calculated)


median = calculate_median()
print(f"Median is: {median/10000}")
