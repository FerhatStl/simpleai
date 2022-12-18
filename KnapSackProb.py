from abc import ABC
import random

from simpleai.search import SearchProblem, hill_climbing, genetic

capacityOfBackpack = int(input('Please enter backpack Capacities: '))


class KnapsackProblem(SearchProblem, ABC):
    """Knapsack problem."""
    itemSize = int(input('Please write how many items: '))
    user_input = input('Please enter values of items(Leave a space for each item value Ex: 1 2 5 3) : ')

    my_tuple_values = tuple(int(item) for item in user_input.split())

    print(my_tuple_values)

    user_input = input('Please enter weights of items(Leave a space for each item value Ex: 10 8 4 9) : ')

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

    def _is_valid(self, g):
        total = 0
        w = 0
        for x in g:
            if x == 1:
                total += valuesAndWeights[1][w]
            w += 1
        print("TOTAL: ",total," ","Capacity: ",capacityOfBackpack)
        return total <= capacityOfBackpack

    def actions(self, s):

        return [a for a in self._actions if self._is_valid(self.result(s, a))]

    def result(self, s, a):
        tempState = tuple(s)
        sendState = []
        for w in range(len(s)):
            if a == ('Change item {}'.format(w)):
                if s[w] == 0:
                    s[w] = 1
                else:
                    s[w] = 0
            sendState.append(s[w])

        if self._is_valid(sendState):
            return sendState
        else:
            return tempState

    def value(self, s):
        total = 0
        i = 0
        for x in s:
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

    def mutate(self, s):
        while True:
            mutation = random.choice(s)
            if s[mutation] == 0:
                s[mutation] = 1
            else:
                s[mutation] = 0
            if self._is_valid(s):
                return s

    def generate_random_state(self):
        while True:
            rnd_state = []
            for _ in range(len(valuesAndWeights[0])):
                k = random.randint(0, 1)  # decide on a k each time the loop runs
                rnd_state.append(k)
            if self._is_valid(rnd_state):
                return rnd_state


problem = KnapsackProblem(initial_state=KnapsackProblem.state)

result = hill_climbing(problem)
print(result.path())
print(result.state)
print(result.value)


# problem2 = KnapsackProblem(initial_state=KnapsackProblem.state)
# result2 = genetic(problem2, population_size=100, mutation_chance=0.1, iterations_limit=0, viewer=None)
# print(result2.path())
# print(result2.state)

# problem2 = KnapsackProblem(initial_state=KnapsackProblem.state)
# result2 = hill_climbing_random_restarts(problem2, restarts_limit=10, iterations_limit=0, viewer=None)
# print(result2.path())
# print(result2.state)


# problem2 = KnapsackProblem(initial_state=KnapsackProblem.state)
# result2 = genetic(problem2, population_size=100, mutation_chance=0.1, iterations_limit=0, viewer=None)
# print(result2.path())
# print(result2.state)

#problem2 = KnapsackProblem(initial_state=KnapsackProblem.state)
#result3 = genetic(problem2, population_size=50)
#print(result3.path())
#print(result3.value)
