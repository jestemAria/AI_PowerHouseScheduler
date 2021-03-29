from random import randint
powerhouse = []
periods = []
number_of_units = 0
number_of_periods = 0
selected_units = []
capacity = 0


def read_file_1():
    file = open("File1.txt", "r")
    global number_of_units
    number_of_units = int(file.readline())
    print("Number of units =", number_of_units)

    for number in range(int(number_of_units)*3):
        data = file.readline()
        powerhouse.append(data)
    file.close()

    count = 0
    print("Unit information :")
    while count < int(number_of_units)*3:
        print("------------------------------------------")
        print("Unit number", powerhouse[count], end='')
        print("Unit capacity", powerhouse[count+1], end='')
        print("Repair period", powerhouse[count+2], end='')
        count = count+3
    print("\n\n")
    print("==========================================")
    return number_of_units


def read_file_2():
    file = open("File2.txt", "r")
    global number_of_periods
    number_of_periods = int(file.readline())
    print("Number of periods =", number_of_periods)

    for number in range(int(number_of_periods)*2):
        data = file.readline()
        periods.append(data)
    file.close()

    count = 0
    print("Period information:")
    while count < int(number_of_periods)*2:
        print("------------------------------------------")
        print("Period number", periods[count], end='')
        print("Required :", periods[count+1], end='')
        count = count+2
    print("\n\n")
    print("==========================================")


def generate_solution():
    print("\n\n<<<<<<Generating solution>>>>>>")
    unit = new_unit()
    if unit is None:
        print("Not enough units for this period")
    global capacity
    capacity = int(powerhouse[(unit * 3) - 2])
    print("Capacity:", capacity)

    period_counter = 1
    required = int(periods[(period_counter * 2) - 1])
    print("Period", period_counter, "required", required)
    while capacity <= required:
        unit = new_unit()
        capacity = capacity + int(powerhouse[(unit * 3) - 2])
        print("Capacity:", capacity)
    period_counter = period_counter + 1
    if period_counter == number_of_periods:
        print("All periods finished!")
    else:
        generate_solution()
    capacity = 0
    print("finished")


# def unit_capacity(unit):
#
#
# def period_required(period):


def new_unit():
    new_random_unit = randint(1, int(number_of_units))
    if len(selected_units) >= number_of_units:
        pass
    else:
        for x in selected_units:
            if new_random_unit in selected_units:
                print("tekrari!")
                new_unit()
        selected_units.append(new_random_unit)
        print("Unit", new_random_unit, "selected randomly.")
        return new_random_unit




read_file_1()
read_file_2()
generate_solution()


