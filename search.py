"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    from util import Stack
    fringe = Stack()                # Fringe to manage which states to expand
    fringe.push(problem.getStartState())
    visited = []                    # List to check whether state has already been visited
    path=[]                         # Final direction list
    pathToCurrent=Stack()           # Stack to maintaing path from start to a state
    currState = fringe.pop()
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)
            successors = problem.getSuccessors(currState)
            for child,direction,cost in successors:
                fringe.push(child)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)
        currState = fringe.pop()
        path = pathToCurrent.pop()
    return path


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    from util import Queue
    fringe = Queue()                        # Fringe to manage which states to expand
    fringe.push(problem.getStartState())
    visited = []                            # List to check whether state has already been visited
    tempPath=[]                             # Temp variable to get intermediate paths
    path=[]                                 # List to store final sequence of directions 
    pathToCurrent=Queue()                   # Queue to store direction to children (currState and pathToCurrent go hand in hand)
    currState = fringe.pop()
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)    
            successors = problem.getSuccessors(currState)
            for child,direction,cost in successors:
                fringe.push(child)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)
        currState = fringe.pop()
        path = pathToCurrent.pop()
        
    return path

def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def singleFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of single food search
    """
    # TODO 20
    pass


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    pass


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
