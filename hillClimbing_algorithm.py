from read_files import unit, period, number_of_units, number_of_periods
import read_files
from random import randint
picked_units = []


class HillClimbingAlgorithm:
    def __init__(self):
        pass


def hill():
    total_capacity = 0
    requires = 0

    print("=======================")
    print("| Generating solution |")
    print("=======================\n")

    period_number = 1
    requires = int(period[period_number - 1].period_requirement)
    print("Period number", period_number, "requires", requires)

    while total_capacity <= requires:
        total_capacity += int(unit[select_random_unit()].unit_capacity)
        print("|________Total capacity is now:", total_capacity)





def clear_list():
    pass


def select_random_unit():
    i = 0
    number = randint(1, read_files.number_of_units)
    if len(picked_units) == read_files.number_of_units:
        print("No free unit for use!")
    else:
        while i <= len(picked_units):
            if number in picked_units:
                number = randint(1, read_files.number_of_units)
            else:
                print("|__Unit", number, "Picked randomly!")
                picked_units.append(number)
                print("|_____Current state of picked units:", picked_units)
                i += 1
                break
        return number-1
