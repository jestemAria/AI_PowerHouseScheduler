import read_files
from hillClimbing_algorithm import HillClimbingAlgorithm
import hillClimbing_algorithm
repetition = 100    # if you change this pls go to hillClimbing_algorythm.py and also change value repetition


class Main:

    if __name__ == '__main__':
        read_files.read_file_1()
        read_files.read_file_2()
        for x in range(repetition):
            hillClimbing_algorithm.generate_solution()
        hillClimbing_algorithm.show_bar()
