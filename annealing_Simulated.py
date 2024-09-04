import math
import random
#random.seed(42)

""" made by reut dayan """


def random_queens(list1: list ,n: int):
    return [random.randint(0,n-1) for index in range(n)]


def schedule(t: int) -> float:
    """
       :param t:the temperature
       :return:Returns a temperature if she big from 0.1
       """
    if 1/t > 0.1:
        return 1/t
    return 0


def worse_solution(temp: float, e: float) -> bool:
    """
    :param temp:the temperature
    :param e:the delta
    :return:Returns true in a certain probability
    """
    if temp==0:
        return False
    probability = math.exp(e/temp)
    rand = random.random()
    return rand < probability


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


def neighbor(queens: list):
    """
    :param queens:list that describes the location of the queens
    :return: new list that represents a queens list, where only one queen's position has been changed

    """
    new_queens = queens[:]
    i = random.randint(0, len(queens)-1)
    new_queens[i] = (new_queens[i] + random.randint(-1, 1)) % len(queens)
    return new_queens


def simulated_annealing(initial_solution: list):
    """
    :param initial_solution:list that describes Initial state of a queens on the board
    :return: A solution or the closest solution to the N Queens problem

    """
    current = initial_solution
    current_cost = enemy_cost(current, len(current))
    time = 1
    while True:
        temp = schedule(time)
        if temp == 0:
            return current
        neighbor_q = neighbor(current)
        neighbor_cost = enemy_cost(neighbor_q, len(neighbor_q))
        delta_energy = neighbor_cost - current_cost
        if delta_energy > 0 or worse_solution(delta_energy, temp):
            current = neighbor_q
        time = time + 1


if __name__ == "__main__":
    n = input("enter a number")
    queens = random_queens(list(),int(n))
    print("initial_solution:")
    print(queens)
    print("number of enemy queens:")
    print(enemy_cost(queens, int(n)))
    new_q= simulated_annealing(queens)
    print("final_solution:")
    print(new_q)
    print("number of enemy queens:")
    print(enemy_cost(new_q, len(new_q)))













