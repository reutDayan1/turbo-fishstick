import math
import random
import numpy as np
import matplotlib.pyplot as plt


def enemy_cost1(queens:list):
    """
    :param queens:list that describes the location of the queens
    :return:The number of threats on the board
    """
    count = 0
    for i in range(len(queens)):
        for j in range(i+1,len(queens)):
            if (queens[i] == queens[j]) or (abs(queens[i]-queens[j]) == abs(j-i)):
                count += 1
    return count


def fitness(population):
    """
    :param population:our population
    :return:list of enemy cost  for the population
    """
    fitness_enemy = []
    for i in range(len(population)):
        list1 = population[i]
        count = enemy_cost1(list1)
        fitness_enemy.append(count)
    return fitness_enemy


def min_enemy(current: list, i):
    """
    :param current:list that describes the location of the queens
    :return:the board with the min enemy
    """
    min_current = current[:]
    number_of_enemy = enemy_cost1(min_current)
    for j in range(len(current)):
        copy_current = current[:]
        if current[i] != j:
            copy_current[i] = j
            c = enemy_cost1(copy_current)
            if c < number_of_enemy:
                number_of_enemy = c
                min_current = copy_current
    return min_current


def the_best_neighbor(current):
    """
    :param current:list that describes the location of the queens
    :return:the best neighbor
    """
    min_current = []
    min_enemy1 = float('inf')
    for i in range(len(current)):
        c = min_enemy(current, i)
        if enemy_cost1(c) < min_enemy1:
            min_current = c[:]
            min_enemy1 = enemy_cost1(c)
            if min_enemy1 == 0:
                return min_current
    return min_current


def hill_climbing(p):
    """
    :param p: initial_solution
    :return:list sorted by number of enemy
    """
    current = p
    current_cost = enemy_cost1(current)
    while True:
        neighbor = the_best_neighbor(current)
        neighbor_cost = enemy_cost1(neighbor)
        if current_cost <= neighbor_cost:
            return current
        current = neighbor
        current_cost = enemy_cost1(current)


def sort_by_attacks(positions):
    """

    :param positions: A list of several boards
    :return:A solution or the closest solution to the N Queens problem
    """
    return sorted(positions, key=enemy_cost1)


def all_neighbors(current: list):
    """

    :param current:list that describes the location of the queens
    :return:A list of al the possible neighbors
    """
    list_neighbors = []
    for neighbor in current:
        for index in range(len(neighbor)):
            for j in range(len(neighbor)):
                if neighbor[index] != j:
                    copy_neighbor = neighbor[:]
                    copy_neighbor[index] = j
                    list_neighbors.append(copy_neighbor)
    return list_neighbors


def k_beams(p):
    """

    :param p:list that describes k board  of  queens
    :return:A solution or the closest solution to the N Queens problem
    """
    best_solution = None
    best_cost = float('inf')
    k = len(p)
    for index in range(7):
        neighbors = all_neighbors(p)
        sorted_list = sort_by_attacks(neighbors)
        new_p = []
        for i in range(k):
            if enemy_cost1(sorted_list[i]) == 0:
                return sorted_list[i]
            new_p.append(sorted_list[i])
        p = new_p
    return p[0]


def random_queens(list1: list, n: int):
    for index in range(int(n)):
        list1.append(random.randint(0, int(n) - 1))
    return list1


def plot_results(k_values, k_beams_success, try_try_again_success):
    plt.plot(k_values, k_beams_success, label='K-Beams Success', marker='o', linestyle='-')
    plt.plot(k_values, try_try_again_success, label='Try-Try Success Rate', marker='o', linestyle='-')
    plt.xlabel('Number of Attempts (K)')
    plt.ylabel('Success Rate (%)')
    plt.title('Success Rate Comparison for Different Number of Attempts')
    plt.grid(True)
    plt.legend()
    plt.show()


n = input("enter a number")
k = input("enter k-beams")
trails = [1000, 2000, 3000 ,500]
k_values = [5] * len(trails)
queens = random_queens(list(),int(n))
print("initial_solution of hill climbing:")
print(queens)
print(enemy_cost1(queens))
a = hill_climbing(queens)
print(a)
print(enemy_cost1(a))
list_trytry_trails = []
for emurate in trails:
    sum_enemy = 0
    for i in range(emurate):
        intitial_soulotion = random_queens(list(),int(n))
        final_soulotion = hill_climbing(intitial_soulotion)
        if enemy_cost1(final_soulotion) == 0:
            sum_enemy += 1
    list_trytry_trails.append((sum_enemy/emurate)*100)
print(list_trytry_trails)
list_kbeams_trails = []

for emurate in trails:
    sum_of_kbeams = 0
    for i in range(emurate):
        list11 = []
        for j in range(int(k)):
            list1 = []
            list11.append(random_queens(list1, int(n)))
        a = k_beams(list11)
        if enemy_cost1(a) == 0:
            sum_of_kbeams += 1
    list_kbeams_trails.append((sum_of_kbeams/emurate)*100)
print(list_kbeams_trails)
plot_results(trails, list_kbeams_trails, list_trytry_trails)


