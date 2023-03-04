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
#    print("Start:", problem.getStartState())
#    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """ Start: (34, 16), Start's successors: [((34, 15), 'South', 1), ((33, 16), 'West', 1)]"""
    
    "*** YOUR CODE HERE ***"
    
    initState = problem.getStartState() # initialize the problem start state 
#    print(initState)
    visited = [] # establish my visited nodes
    fringe = Stack() # establish my stack for DFS
    fringe.push((initState, [], 0)) # push the initial state, list to hold directions (return type like tinyMaze), & cost
#    print(fringe)
    
    while not fringe.isEmpty(): # while there are values in the fringe
        curr, path, cost = fringe.pop() # pop off the current node, the current list of actions, and cost 
#        print(curr, actions, cost)
        if curr not in visited: # if the current node is not visited 
            visited.append(curr) # append the current node to visited 
            if problem.isGoalState(curr): # when the initital state becomes the goal state
                return path  # return the list of actions
            else:
                successors = problem.getSuccessors(curr) # get all the successors of the current node
                for nxt, action, cst in successors: # for next node, action, and cost in successors 
                    copy = path.copy()
                    copy.append(action)
                    curr_path = copy
                    new_cost = cost + cst  # add new extra cost to cost 
                    fringe.push((nxt, curr_path, new_cost)) # push this onto the fringe 


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    from util import Queue
# Same code as above, but with a different fringe 
    initState = problem.getStartState() # initialize the problem start state 
#    print(initState)
    visited = [] # establish my visited nodes
    fringe = Queue() # establish my queue for BFS
    fringe.push((initState, [], 0)) # push the initial state, list to hold directions (return type like tinyMaze), & cost
#    print(fringe)
    
    while not fringe.isEmpty(): # while there are values in the fringe
        curr, path, cost = fringe.pop() # pop off the current node, the current list of actions, and cost 
#        print(curr, actions, cost)
        if curr not in visited: # if the current node is not visited 
            visited.append(curr) # append the current node to visited 
            if problem.isGoalState(curr): # when the initital state becomes the goal state
                return path  # return the list of actions
            else:
                successors = problem.getSuccessors(curr) # get all the successors of the current node
                for nxt, action, cst in successors: # for next node, action, and cost in successors 
                    copy = path.copy()
                    copy.append(action)
                    curr_path = copy
                    new_cost = cost + cst  # add new extra cost to cost 
                    fringe.push((nxt, curr_path, new_cost)) # push this onto the fringe 


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
        # TODO 19
    from util import PriorityQueue
    initState = problem.getStartState() # initialize the problem start state 
#    print(initState)
    visited = [] # establish my visited nodes
    fringe = PriorityQueue() # establish priority queue for UCS
    fringe.push((initState, [], 0), 0) # push initState, list of direction, cost AND priority 

    while not fringe.isEmpty(): # while there are values in the fringe
        curr, path, cost = fringe.pop()  # pop off the current node, the current list of actions, and cost 
 #        print(curr, actions, cost)
        if curr not in visited: # if the current node is not visited 
            visited.append(curr) # append the current node to visited 
            if problem.isGoalState(curr): # when the initital state becomes the goal state
                return path  # return the list of actions
            else:
                successors = problem.getSuccessors(curr) # get all the successors of the current node
                for nxt, action, cst in successors: # for next node, action, and cost in successors 
                    copy = path.copy()
                    copy.append(action)
                    curr_path = copy
                    new_cost = cost + cst # add new extra cost to cost 
                    fringe.push((nxt, curr_path, new_cost), new_cost) # push onto the fringe, but push new priority value which is cost 



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
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"    # TODO 22   
    from util import PriorityQueue
    initState = problem.getStartState() # initialize the problem start state 
#    print(initState)
    visited = [] # establish my visited nodes
    fringe = PriorityQueue() # establish priority queue for UCS
    fringe.push((initState, [], 0), 0) # push initState, list of direction, cost AND priority 

    while not fringe.isEmpty(): # while there are values in the fringe
        curr, path, cost = fringe.pop()  # pop off the current node, the current list of actions, and cost 
 #        print(curr, actions, cost)
        if curr not in visited: # if the current node is not visited 
            visited.append(curr) # append the current node to visited 
            if problem.isGoalState(curr): # when the initital state becomes the goal state
                return path  # return the list of actions
            else:
                successors = problem.getSuccessors(curr) # get all the successors of the current node
                for nxt, action, cst in successors: # for next node, action, and cost in successors 
                    copy = path.copy()
                    copy.append(action)
                    curr_path = copy
                    new_cost = cost + cst # add new extra cost to cost 
                    # print(heur)                 # heuristic is function defined as nullHeuristic
                    heur = heuristic(nxt, problem) + new_cost # calculate new heuristic value 
                    fringe.push((nxt, curr_path, new_cost), heur) # push onto the fringe, and push the heuristic as the new priority principle 




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
