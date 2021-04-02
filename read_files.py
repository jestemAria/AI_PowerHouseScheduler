from power_plant import PowerPlant
from period_plant import PeriodPlant

# Global Variables:
number_of_units = 0
number_of_periods = 0
unit = []
period = []


def read_file_1():
    file = open("File1.txt", "r")
    global number_of_units, unit
    number_of_units = int(file.readline())
    print("Number of units :", number_of_units)

    for index in range(int(number_of_units)):
        unit_id = file.readline()
        unit_capacity = file.readline()
        unit_maintenance_period = file.readline()
        unit.append(PowerPlant(unit_id, unit_capacity, unit_maintenance_period))
        print("------------------------")
        print("Unit ID :", unit_id, end="")
        print("Unit capacity :", unit_capacity, end="")
        print("Maintenance Period :", unit_maintenance_period, end="")
    file.close()
    print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-\n")


def read_file_2():
    file = open("File2.txt", "r")
    global number_of_periods, period
    number_of_periods = int(file.readline())
    print("Number of periods :", number_of_periods)

    for index in range(int(number_of_periods)):
        period_id = file.readline()
        period_requirement = file.readline()
        period.append(PeriodPlant(period_id, period_requirement))
        print("---------------------------")
        print("Period ID :", period_id, end="")
        print("Period Requirement :", period_requirement, end="")
    file.close()
    print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
