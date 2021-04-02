from read_files import unit, period, number_of_units, number_of_periods
import read_files
from random import randint
picked_units = []


class HillClimbingAlgorithm:
    def __init__(self):
        pass


def generate_first_solution():
    new_unit = 0
    total_capacity = 0
    total_periods = int(read_files.number_of_periods)

    print("=======================")
    print("| Generating solution |")
    print("=======================\n")

    period_number = 1
    while period_number <= total_periods:
        requires = int(period[period_number - 1].period_requirement)
        print("Period number", period_number, "requires", requires)

        while total_capacity <= requires:
            new_unit = select_random_unit()
            if new_unit is None:
                break
            else:
                total_capacity += int(unit[new_unit].unit_capacity)
                print("       Total capacity is now:", total_capacity)
                if total_capacity == requires:
                    break

        if new_unit is None:
            print("Solution Failed!")
            break
        period_number += 1
        total_capacity = 0
        
    if new_unit is not None:
        print("\n($) Solution was Successful!\n")


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
                print("    Unit", number, "Picked randomly!")
                picked_units.append(number)
                print("       Current state of picked units:", picked_units)
                i += 1
                break
        return number-1
