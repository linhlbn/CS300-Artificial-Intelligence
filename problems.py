import util
from game import Directions, Actions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        
       # TODO 1
       # Initialize the start state, walls, and cost function
       self.start = (startingGameState.getPacmanPosition(), startingGameState.getFood())
       self.walls = startingGameState.getWalls()
       self.costFn = lambda x: 1
       self.startingGameState = startingGameState
       self._expanded = 0 # DO NOT CHANGE
       self.heuristicInfo = {} # A dictionary for the heuristic to store information


    def getStartState(self):
        
      # TODO 2
      # Return the start state
      return self.start


    def isGoalState(self, state):

      # TODO 3
      # Check if there is no more food left
      return state[1].count() == 0


    def getSuccessors(self, state):

      # TODO 4
      # Return a list of successors with their actions and costs
        successors = []
        self._expanded += 1 # DO NOT CHANGE
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append( ( ((nextx, nexty), nextFood), direction, 1) )
        return successors

    def getCostOfActions(self, actions):

     # TODO 5 
     # Return the sum of costs of all actions
     #return sum([self.costFn(action) for action in actions])
        """Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999"""
        x,y= self.getStartState()[0]
        cost = 0
        for action in actions:
            # figure out the next state and see whether it's legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999
            cost += 1
        return cost     


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 6
        pass

    def getStartState(self):
        # TODO 7
        pass

    def isGoalState(self, state):
        # TODO 8
        pass

    def getSuccessors(self, state):
        # TODO 9
        pass

    def getCostOfActions(self, actions):
        # TODO 10
        pass