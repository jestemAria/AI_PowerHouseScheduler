from read_files import unit, period, number_of_units, number_of_periods
import read_files
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

picked_units = []
solution = []
solution_repair = []
net_reserve = []
visited_units = []
minimum_needed = []
produced = []

must_repair = []
in_repair = []
repaired = []

unit_maintenance = 0
min_ele = 0
counter_control_repair = 0
counter_control_forward = 0
minimum_net_reserve = 0
is_failed = False

best_net_reserve = 0
repetition = 100  # if you change this pls go to main.py and also change value repetition


class HillClimbingAlgorithm:
    def __init__(self):
        pass


def generate_solution():
    global solution
    global solution_repair
    global picked_units
    global unit_maintenance
    global counter_control_repair
    global counter_control_forward
    global minimum_net_reserve
    global must_repair
    global in_repair
    global repaired
    global produced
    global minimum_needed
    global net_reserve
    global is_failed
    
    is_failed = False

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
            is_failed = True
            break

        solution.append(picked_units)
        minimum_needed.append(requires)
        produced.append(total_capacity)
        net_reserve.append(total_capacity - requires)
        period_number += 1
        total_capacity = 0
        picked_units = []

    if is_failed:
        return

    if new_unit is not None:
        print("\nSolution Successful -> Supplying Energy\n")

    for x in range(read_files.number_of_units):
        must_repair.append(x+1)

    for y in range(read_files.number_of_periods):
        solution_repair.append([])
        # print(solution_repair)

    period_number = 1

    is_failed = False

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
                        is_failed = True
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

                if is_failed:
                    break

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
                    if period_number - 1 < read_files.number_of_periods:  ###############################
                        solution_repair[period_number - 1].append(new_unit + 1)
                    else:
                        print("Solution Failed! --[]")
                        is_failed = True
                        break

                period_number += 1
            else:
                forward_period = 0
                picked_units.remove(new_unit + 1)
                if is_failed:
                    break
        else:
            picked_units.remove(new_unit + 1)
            if is_failed:
                break

        if len(must_repair) == 1:
            period_number += 1
        if counter_control_repair == read_files.number_of_periods * 5:
            print("\n!!! Solution Failed !!!\n")
            is_failed = True
            break

        counter_control_repair += 1
        show_unit_maintenance_status()

        # print(index_of_minimum())
        is_failed = False

    if is_failed:
        picked_units = []
        must_repair = []
        in_repair = []
        repaired = []
        solution = []
        solution_repair = []
        minimum_needed = []
        produced = []
        net_reserve = []
        counter_control_forward = 0
        counter_control_repair = 0
        all_net_reserves.append("0")
        return

    if index_of_minimum() == 0:
        for x in range(len(solution)-1):
            # print(x)
            if produced[x] - minimum_needed[x] < produced[x] - minimum_needed[x + 1] and produced[x +1] >= minimum_needed[x]:
                solution[x], solution[x + 1] = solution[x + 1], solution[x]
                solution_repair[x], solution_repair[x + 1] = solution_repair[x + 1], solution_repair[x]
                produced[x], produced[x + 1] = produced[x + 1], produced[x]
                print("Swapped! -R")
                break
    elif index_of_minimum() == read_files.number_of_periods - 1:
        for x in range(len(solution)-1, 1, -1):
            # print(x)
            if produced[x] - minimum_needed[x] < produced[x] - minimum_needed[x-1] and produced[x-1] >= minimum_needed[x]:
                solution[x], solution[x-1] = solution[x-1], solution[x]
                solution_repair[x], solution_repair[x-1] = solution_repair[x-1], solution_repair[x]
                produced[x], produced[x - 1] = produced[x - 1], produced[x]
                print("Swapped! -L")
                break
    else:
        for x in range(1, len(solution)-2, 1):
            # print(x)
            if produced[x] - minimum_needed[x] < produced[x] - minimum_needed[x + 1] and produced[x +1] >= minimum_needed[x]:
                solution[x], solution[x + 1] = solution[x + 1], solution[x]
                solution_repair[x], solution_repair[x + 1] = solution_repair[x + 1], solution_repair[x]
                produced[x], produced[x + 1] = produced[x + 1], produced[x]
                print("Swapped! -M")
                break
            if produced[x] - minimum_needed[x] < produced[x] - minimum_needed[x-1] and produced[x-1] >= minimum_needed[x]:
                solution[x], solution[x-1] = solution[x-1], solution[x]
                solution_repair[x], solution_repair[x-1] = solution_repair[x-1], solution_repair[x]
                produced[x], produced[x - 1] = produced[x - 1], produced[x]
                print("Swapped! -L")
                break

        # recalculate()

    show_solution()

    save_result()

    picked_units = []
    must_repair = []
    in_repair = []
    repaired = []
    solution = []
    solution_repair = []
    minimum_needed = []
    produced = []
    net_reserve = []
    counter_control_forward = 0
    counter_control_repair = 0


def unit_completely_maintenance():
    if unit_maintenance == 0:
        return True
    else:
        return False


solution_copy = []
solution_repair_copy = []
minimum_needed_copy = []
produced_copy = []
net_reserve_copy = []

name = []
all_net_reserves = []


def save_result():
    global best_net_reserve
    global solution_copy
    global solution_repair_copy
    global minimum_needed_copy
    global produced_copy
    global net_reserve_copy

    if min(net_reserve) > best_net_reserve:
        best_net_reserve += min(net_reserve)

        solution_copy = []
        solution_repair_copy = []
        minimum_needed_copy = []
        produced_copy = []
        net_reserve_copy = []

        solution_copy.extend(solution)
        solution_repair_copy.extend(solution_repair)
        minimum_needed_copy.extend(minimum_needed)
        produced_copy.extend(produced)
        net_reserve_copy.extend(net_reserve)

    if best_net_reserve > 0:
        print("+++++++++++++++++++++++++++++++++++++")
        print("Best Result Until Now :")

        print("Units Under Supply:", solution_copy)
        print("Units Under Repair:", solution_repair_copy)
        print("Power Produced Per Period:", produced_copy)
        print("Net Reserve:", net_reserve_copy)
        print(" -> best net reserve globally is:", min(net_reserve_copy))
        print("+++++++++++++++++++++++++++++++++++++")

    for x in range(read_files.number_of_periods):
        if len(name) < read_files.number_of_periods:
            name.append(x)

    all_net_reserves.append(min(net_reserve))


def show_unit_maintenance_status():
    print("         Unit maintenance status:")
    print("         |_must repair :", must_repair)
    print("         |_in repair :", in_repair)
    print("         |_repaired :", repaired)


def show_solution():
    print("\n\n")
    print("Units Under Supply:", solution)
    print("Units Under Repair:", solution_repair)
    print("Minimum Needed Per Period:", minimum_needed)
    print("Power Produced Per Period:", produced)

    for x in range(len(solution)):
        net_reserve[x] = produced[x] - minimum_needed[x]

    print("Net Reserve:", net_reserve)
    print("Minimum Net Reserve Is:", min(net_reserve), "\n")


def index_of_minimum():
    for x in range(len(net_reserve)):
        if net_reserve[x] == min(net_reserve):
            # print(x)
            return x


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


def show_bar():

    barWidth = 0.3

    r1 = np.arange(len(minimum_needed_copy))
    r2 = [x + barWidth for x in r1]

    plt.bar(r1, minimum_needed_copy, width=barWidth, color='blue', edgecolor='black', capsize=7, label='Minimum Required')

    plt.bar(r2, produced_copy, width=barWidth, color='cyan', edgecolor='black', capsize=7, label='Produced Energy')

    plt.xticks([r + barWidth for r in range(len(minimum_needed_copy))], name)
    plt.ylabel('Energy (MegaWatt)')
    plt.xlabel('Period Number')
    plt.legend()
    plt.show()

    df = pd.DataFrame({'x_axis': range(0, repetition), 'y_axis': all_net_reserves})

    sns.set_theme()

    # Plot
    plt.plot('x_axis', 'y_axis', data=df, marker='o', color='mediumvioletred')
    plt.ylabel('Net Reserve (Mega Watt)')
    plt.xlabel('Repetition In Time')
    plt.show()

