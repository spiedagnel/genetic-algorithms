from robotic_controllers import maze as mz
from robotic_controllers import genetic_algorithm


MAX_GENERATIONS = 1000

def main():

    # 0 = Empty
    # 1 = Wall
    # 2 = Starting position
    # 3 = Route
    # 4 = Goal position

    maze = mz.Maze([[0, 0, 0, 0, 1, 0, 1, 3, 2],
                [1, 0, 1, 1, 1, 0, 1, 3, 1],
                [1, 0, 0, 1, 3, 3, 3, 3, 1],
                [3, 3, 3, 1, 3, 1, 1, 0, 1],
                [3, 1, 3, 3, 3, 1, 1, 0, 0],
                [3, 3, 1, 1, 1, 1, 0, 1, 1],
                [1, 3, 0, 1, 3, 3, 3, 3, 3],
                [0, 3, 1, 1, 3, 1, 0, 1, 3],
                [1, 3, 3, 3, 3, 1, 1, 1, 4]])

    ga = genetic_algorithm.GeneticAlgorithm(200, 0.05, 0.9, 2, 10)
    population = ga.init_population(128)

    generation = 1




if __name__ == "__main__":
    main()

