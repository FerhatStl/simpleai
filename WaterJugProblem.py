import sys
from simpleai.search.traditional import (breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost)
from simpleai.search.models import SearchProblem
from simpleai.search.viewers import BaseViewer


def ListFiller(listName, string):
    for i in range(len(listName)):
        a = i + 1
        x = int(input(string + str(a) + ": "))
        listName[i] = x


def LogicalControl():
    # The function determined to control that target is not larger that capacity for each jug.
    for i in range(len(capacity)):
        if(target[i] > capacity[i]):
            print("The target value of jug", str(i+1), """is more than its capacity.
The execution will stop.""")
            sys.exit()

capacity = [8, 5, 3]
target = [4, 4, 0]
graph_search_bool = True


class WaterJugProblem(SearchProblem):

    def _init_(self, initial_state=None, viewer = None):
        self.initial_state = initial_state
        self.viewer = viewer

    def actions(self, state):
        return ["Fill1", "Fill2", "Fill3", "Empty1", "Empty2", "Empty3", "Pour1to2", "Pour1to3", "Pour2to1", "Pour2to3",
                "Pour3to1", "Pour3to2"]

    def result(self, state, action):

        next_state = list(state)

        def PourToOther(a, b):
            next_state[b] = min(state[a] + state[b], capacity[b])
            next_state[a] = state[a] - (next_state[b] - state[b])

        if action == "Fill1":
            next_state[0] = capacity[0]
        elif action == "Fill2":
            next_state[1] = capacity[1]
        elif action == "Fill3":
            next_state[2] = capacity[2]
        elif action == "Empty1":
            next_state[0] = 0
        elif action == "Empty2":
            next_state[1] = 0
        elif action == "Empty3":
            next_state[2] = 0
        elif action == "Pour1to2":
            PourToOther(0, 1)
        elif action == "Pour1to3":
            PourToOther(0, 2)
        elif action == "Pour2to1":
            PourToOther(1, 0)
        elif action == "Pour2to3":
            PourToOther(1, 2)
        elif action == "Pour3to1":
            PourToOther(2, 0)
        elif action == "Pour3to2":
            PourToOther(2, 1)

        return tuple(next_state)

    def cost(self, state, action, state2):
        if action == "Fill1":
            return capacity[0] - state[0]
        elif action == "Fill2":
            return capacity[1] - state[1]
        elif action == "Fill3":
            return capacity[2] - state[2]
        elif action == "Empty1":
            return state[0]
        elif action == "Empty2":
            return state[1]
        elif action == "Empty3":
            return state[2]
        else:
            return 1

    def is_goal(self, state):
        return bool(list(state) == target)

class main:
    print("""----------------------------------------------------------
-------------- Welcome To Water Jug Problem --------------
----------------------------------------------------------
    """)

    print("""The pre defined value of:
    Capacity is :""", capacity, """
    Target is :""", target)
    firstInput = input("Do you want to redefine them?(Y/N):")
    if firstInput == "Y" or firstInput == "1" or firstInput == "y":
        ListFiller(capacity, "Please write capacity of jug ")
        print('Capacity: ', capacity)
        print("----------------------------------------------------------")
        ListFiller(target, "Please write target liter of jug ")
        print('Target: ', target)
        print("----------------------------------------------------------")
        LogicalControl()
    elif firstInput == "N" or firstInput == "0" or firstInput == "n":
        pass
    else:
        print("----------------------------------------------------------")
        print("Unexpected input. The system will continue with predefined values.")

    print("Graph Search:", graph_search_bool)
    boolOfGraphSearch = input("Do you want to use graph sarch?(Y/N)")
    if boolOfGraphSearch == "Y" or boolOfGraphSearch == "y" or boolOfGraphSearch == 1:
        pass
    elif boolOfGraphSearch == "N" or boolOfGraphSearch == "n" or boolOfGraphSearch == 0:
        graph_search_bool = False
    else:
        print("----------------------------------------------------------")
        print("Unexpected input. The system will continue with True.")

    print("----------------------------------------------------------")
    print("Graph Search:", graph_search_bool)
    print('Capacity: ', capacity)
    print('Target: ', target)

    print("""--------------------List of Algorithms--------------------
    1. Breadth First Search (BFS)
    2. Depth First Search (DFS)
    3. Uniform Cost Search (UCS)
    4. Depth Limited Search (DLS)
    5. Iterative Deepening Search (IDS)
----------------------------------------------------------""")

    input1 = int(input("Please write the number of the algorithm you want to use: "))
    print("----------------------------------------------------------")
    my_viewer = BaseViewer()
    problem = WaterJugProblem(initial_state=(0, 0, 0))
    if input1 == 1:
        result = breadth_first(problem, graph_search=graph_search_bool , viewer = my_viewer)
    elif input1 == 2:
        result = depth_first(problem, graph_search=graph_search_bool, viewer = my_viewer)
    elif input1 == 3:
        result = uniform_cost(problem, graph_search=graph_search_bool,  viewer = my_viewer)
    elif input1 == 4:
        rakam = int(input("Please define a depth limit(None is default):"))
        if rakam > 0:
            depthLimit = rakam
        else:
            depthLimit = None
        result = limited_depth_first(problem, depth_limit=depthLimit, graph_search=graph_search_bool, viewer = my_viewer)
        print("Depth Limit: ", depthLimit)
    elif input1 == 5:
        result = iterative_limited_depth_first(problem, graph_search=graph_search_bool, viewer = my_viewer)
    else:
        print("The input is not valid.")

    print("Graph Search:", graph_search_bool)
    print("Resulting State: ", result.state)
    print("Resulting path:")
    for i in range(len(result.path())):
        print(i, " . ", result.path()[i])
    print("viewer: stats:", my_viewer.stats)