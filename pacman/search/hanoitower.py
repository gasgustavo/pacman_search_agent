
from copy import deepcopy
import search
import random

# Module Classes

class HanoiTowerSearchProblem(search.SearchProblem):
    """
      Implementation of a SearchProblem for the  Hanoi Tower problem

      Each state is represented by an instance of an Hanoi Tower.
    """
    def __init__(self, hanoi_size, slot_size):
        "Creates a new Hanoi Tower which stores search information."
        self.hanoi_size = hanoi_size
        self.slot_size = slot_size
        self.hanoi_tower = createRandomHanoiTower(self.hanoi_size, self.slot_size)

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.hanoi_tower

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        condition_1 = sum([len(i) > 0 for i in state]) == 1  # all objects are in same space
        condition_2 = [i == sorted(i, reverse=True) for i in state if len(i) > 0][0]  # ordered objects

        return condition_1 and condition_2

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successors = []
        for leaving_position in range(self.slot_size):
            for arriving_position in range(self.slot_size):
                leaving_stack = state[leaving_position]
                if state[leaving_position]:
                    arriving_stack = state[arriving_position]
                    if arriving_stack:
                        if leaving_stack[-1] < arriving_stack[-1]:
                            successor = deepcopy(state)
                            successor[arriving_position].append(successor[leaving_position].pop())
                            successors.append((successor, [leaving_position, arriving_position], 1))
                    else:
                        successor = deepcopy(state)
                        successor[arriving_position].append(successor[leaving_position].pop())
                        successors.append((successor, [leaving_position, arriving_position], 1))

        return successors




def createRandomHanoiTower(hanoi_size, slot_size):
    """
      hanoi_size: de maximum size of a hanoi piece
      slot_size:  number of slots that you can put your hanoi pieces

      Creates a random hanoi tower
      """
    hanoi_tower = [[] for _ in range(slot_size)]
    for i in range(1, hanoi_size + 1):
        random_position = random.randint(0, slot_size - 1)
        hanoi_tower[random_position].append(i)
    for sublist in hanoi_tower:
        random.shuffle(sublist)
    return hanoi_tower

if __name__ == '__main__':

    problem = HanoiTowerSearchProblem(hanoi_size=5, slot_size=3)
    hanoi_tower = problem.getStartState()
    print('A random hanoi tower: {}'.format('--'.join([str(i) for i in hanoi_tower])))
    path = search.breadthFirstSearch(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    i = 1
    for action in path:
        hanoi_tower[action[1]].append(hanoi_tower[action[0]].pop())
        print('new configuration: {}'.format('--'.join([str(i) for i in hanoi_tower])))

        input("Press return for the next state...")   # wait for key stroke
