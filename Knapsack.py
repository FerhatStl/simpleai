import random
from typing import Tuple

from simpleai.search.local import hill_climbing, hill_climbing_random_restarts, genetic

from simpleai.search.models import SearchProblem

capacity = 12
weights = [5, 3, 7, 2]
values = [12, 5, 10, 7]
value = 0
amount_Of_Item = len(weights)


# state içinde 1,2,3,4 tutulacak.
# eşya sayısı değişken.

class KnapsackProblem(SearchProblem):

    def _init_(self, initial_state=None, viewer=None):
        self.initial_state = initial_state
        self.viewer = viewer

    def actions(self, state):
        liste = [_ for _ in range(amount_Of_Item)]
        return liste

    def result(self, state, action):
        next_state = list(state)
        exist = False
        for _ in list(state):
            if action == _:
                exist = True

        if not exist:
            next_state.append(action)
        return tuple(next_state)

    def cost(self, state, action, state2):
        return weights[action]

    def value(self, state):
        return sum(int(values[int(int(_) - 1)]) for _ in list(state))

    def generate_random_state(self):
        liste = (1, 2, 3, 4)
        return random.choice(liste)

    def crossover(self, state1, state2):
        pass

    def mutate(self, state):
        pass


if __name__ == '__main__':
    problem = KnapsackProblem(initial_state='')
    hill_climbing(problem)
    #hill_climbing_random_restarts(problem, 100)
