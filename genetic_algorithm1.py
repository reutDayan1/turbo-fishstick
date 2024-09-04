import heapq
import math
import random
import numpy as np
""" made by reut dayan"""

m = 100
size = 8


def mutate(child,  mutation_rate=0.1):
    """

    :param child: The child created from both parents
    :param mutation_rate:The probability of changing the position of a queen
    :return:the child with the change according to the probability
    """
    child1 = child[:]
    if random.random() < mutation_rate:
        i = random.randint(0, len(child)-1)
        child[i] = random.randint(0, len(child)) % len(child)
    return child


def tournament_selection(population: list):
    """
    :param population: our population
    :return: the best parent from k individuals
    """
    if len(population) <= 8:
        k = int(len(population) / 2)
    else:
        k = int(len(population) / 3)
    parent_list = random.sample(population, k)
    parent_list.sort(key=lambda x: enemy_cost(x,len(x)))
    return parent_list[0]


def enemy_cost(queens: list, n: int):

    """
    :param queens:list that describes the location of the queens
    :param n: list length
    :return:The number of threats on the board
    """
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (queens[i] == queens[j]) or (abs(queens[i]-queens[j]) == abs(j-i)):
                count += 1
    return count


def reproduce(x, y):
    """

    :param x: parent x
    :param y: parent y
    :return: a child from the parents
    """
    n = len(x)
    child = x[:n // 2] + y[n // 2:]
    return child


def min_individual(population):
    """

    :param population: our population
    :return: the individual with the fewest threats
    """
    low_enemy_cost = float('inf')
    low_enemy = []
    for i in population:
        cost = enemy_cost(i, len(i))
        if cost < low_enemy_cost:
            low_enemy_cost = enemy_cost(i, len(i))
            low_enemy = i[:]
    return low_enemy


def genetic_algorithm(population: list):
    """

    :param population:
    :return:A solution or the closest solution to the N Queens problem
    """
    for i in range(m):
        new_population = []
        for j in range(int(len(population))):
            x = tournament_selection(population)
            y = tournament_selection(population)
            child = reproduce(x, y)
            child = mutate(child)
            if enemy_cost(child, len(child)) == 0:
                return child
            new_population.append(child)
        population = new_population
    return min_individual(population)


def random_queens(list1: list ,n: int):
    return [random.randint(0,n-1) for index in range(n)]


if __name__ == "__main__":
    n = int(input("enter a number of Nqueens"))
    list11 = []
    for i in range(size):
        list1 = []
        list11.append(random_queens(list1,n))
    print(list11)
    list12 = genetic_algorithm(list11)
    print(list12)
    print(enemy_cost(list12, len(list12)))

