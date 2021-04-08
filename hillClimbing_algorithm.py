from read_files import unit, period, number_of_units, number_of_periods
import read_files
from random import randint
picked_units = []
solution = []
solution_repair = []

must_repair = []
in_repair = []
repaired = []

unit_maintenance = 0

counter_control_repair = 0
counter_control_forward = 0


class HillClimbingAlgorithm:
    def __init__(self):
        pass


def generate_first_solution_work():
    global solution
    global picked_units
    global unit_maintenance
    global counter_control_repair
    global counter_control_forward
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

        solution.append(picked_units)
        period_number += 1
        total_capacity = 0
        picked_units = []

    if new_unit is not None:
        print("\nSolution Successful -> Supplying Energy\n")

    for x in range(read_files.number_of_units):
        must_repair.append(x+1)

    for y in range(read_files.number_of_periods):
        solution_repair.append([])
        print(solution_repair)

    period_number = 1

    while len(must_repair) > 0:
        new_unit = select_random_unit()
        forward_period = int(unit[new_unit].unit_maintenance_period)

        if period_number > read_files.number_of_periods:
            period_number = 1
        print("      in period", period_number, "unit", solution[period_number - 1], "used")
        if new_unit + 1 not in solution[period_number - 1]:
            if period_number - 1 + forward_period - 1 <= read_files.number_of_periods:
                while forward_period > 0:

                    if counter_control_forward == read_files.number_of_periods * 5:
                        print("Solution Failed -> No way to repair units because of unit's orders ")
                        break
                    # print("forward num is:", forward_period)
                    if period_number > read_files.number_of_periods:
                        period_number = 1
                    # print("period num is:", period_number)
                    if period_number - 1 + forward_period - 1 < read_files.number_of_periods:
                        if new_unit + 1 not in solution[period_number - 1 + forward_period - 1]:
                            forward_period -= 1
                        else:
                            period_number += forward_period
                            counter_control_forward += 1
                            # print(counter_control_forward)
                    else:
                        period_number = 1
                        forward_period = 0

                # if

                in_repair.append(new_unit + 1)
                must_repair.remove(new_unit + 1)
                show_unit_maintenance_status()
                print("             Unit", new_unit + 1, "have", int(unit[new_unit].unit_maintenance_period),
                      "period for maintenance")

                unit_maintenance = int(unit[new_unit].unit_maintenance_period)
                unit_maintenance -= 1

                solution_repair[period_number - 1].append(new_unit + 1)

                print("             Unit", new_unit + 1, "have", unit_maintenance,
                      "period for maintenance")

                while True:
                    if unit_completely_maintenance():
                        in_repair.remove(new_unit + 1)
                        repaired.append(new_unit + 1)
                        break
                    unit_maintenance -= 1
                    period_number += 1
                    print("             Unit", new_unit + 1, "need", unit_maintenance,
                          "period for maintenance")
                    solution_repair[period_number - 1].append(new_unit + 1)

                period_number += 1
            else:
                forward_period = 0
                picked_units.remove(new_unit + 1)
        else:
            picked_units.remove(new_unit + 1)

        if len(must_repair) == 1:
            period_number += 1
        if counter_control_repair == read_files.number_of_periods * 5:
            print("\n!!! Solution Failed !!!\n")
            break

        counter_control_repair += 1
        show_unit_maintenance_status()

        print(solution)
        print(solution_repair)



def unit_completely_maintenance():
    if unit_maintenance == 0:
        return True
    else:
        return False


def show_unit_maintenance_status():
    print("         Unit maintenance status:")
    print("         |_must repair :", must_repair)
    print("         |_in repair :", in_repair)
    print("         |_repaired :", repaired)


def select_random_unit():
    i = 0
    global picked_units
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
                # print("       Current state of picked units:", picked_units)
                i += 1
                break
        return number-1
