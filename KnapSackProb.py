import sys
from abc import ABC
import random
from simpleai.search import SearchProblem, hill_climbing, genetic, hill_climbing_random_restarts

print("""----------------------------------------------------------
-------------- Welcome To Knapsack Problem ---------------
----------------------------------------------------------""")
capacityOfBackpack = int(input('Please enter backpack Capacities: '))


class KnapsackProblem(SearchProblem, ABC):
    itemSize = int(input('Please write how many items do you have: '))
    user_input = input('Please enter values of items(Leave a space for each item value Ex: 1 2 5 3) : ')

    my_tuple_values = tuple(int(item) for item in user_input.split())

    print(my_tuple_values)

    user_input = input('Please enter weights of items(Leave a space for each item value (Ex: 10 8 4 9): ')

    my_tuple_weights = tuple(int(item) for item in user_input.split())

    print(my_tuple_weights)

    global valuesAndWeights
    valuesAndWeights = [my_tuple_values, my_tuple_weights]

    print("************************************")
    print("Capacity: ", capacityOfBackpack)
    print("İtems: ", itemSize)
    print("Values: ", valuesAndWeights[0])
    print("Weights: ", valuesAndWeights[1])
    print("************************************")

    state = [0] * itemSize

    def __init__(self, initial_state=None):
        super().__init__(initial_state)
        self._actions = []

        for x in range(self.itemSize):
            self._actions.append(('Change item {}'.format(x)))

    @staticmethod
    def _is_valid(g):
        total = 0
        w = 0
        for x in g:
            if x == 1:
                total += valuesAndWeights[1][w]
            w += 1
        return total <= capacityOfBackpack

    def actions(self, state):

        return [a for a in self._actions if self._is_valid(self.result(state, a))]

    def result(self, state, action):
        temp_state = list(state)
        for w in range(len(state)):
            if action == ('Change item {}'.format(w)):
                if temp_state[w] == 0:
                    temp_state[w] = 1
                else:
                    temp_state[w] = 0

        if self._is_valid(temp_state):
            return temp_state
        else:
            return state

    def value(self, state):
        total = 0
        i = 0
        for x in state:
            if x == 1:
                total += valuesAndWeights[0][i]
            i += 1
        return total

    def crossover(self, state1, state2):
        while True:
            cut_point = random.randint(0, len(state1))
            child = state1[:cut_point] + state2[cut_point:]
            if self._is_valid(child):
                return child

    def mutate(self, state):
        while True:
            mutation = random.choice(state)
            if state[mutation] == 0:
                state[mutation] = 1
            else:
                state[mutation] = 0
            if self._is_valid(state):
                return state

    def generate_random_state(self):
        while True:
            rnd_state = []
            for _ in range(len(valuesAndWeights[0])):
                k = random.randint(0, 1)  # decide on a k each time the loop runs
                rnd_state.append(k)
            if self._is_valid(rnd_state):
                return rnd_state


if __name__ == '__main__':
    print("""--------------------List of Algorithms--------------------
    1. Genetic
    2. Hill Climbing
    3. Hill Climbing Random Restart
----------------------------------------------------------""")
    while True:
        input1 = int(input("Please write the number of the algorithm you want to use: "))
        print("----------------------------------------------------------")
        problem = KnapsackProblem(initial_state=KnapsackProblem.state)
        if input1 == 1:
            result = genetic(problem, population_size=100, mutation_chance=0.1, iterations_limit=0, viewer=None)
        elif input1 == 2:
            result = hill_climbing(problem, iterations_limit=0, viewer=None)
        elif input1 == 3:
            input2 = int(input("Please write restart limit:"))
            result = hill_climbing_random_restarts(problem, restarts_limit=input2, iterations_limit=0, viewer=None)
        else:
            print("The input is not valid. The program will exit.")
            sys.exit()
        print(result.path())
        print(result.state)
        print(result.value)
