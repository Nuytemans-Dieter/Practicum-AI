# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # Pseudo code:
    # Put current node in 'visited'
    # Put adjacent nodes in 'stack'
    # Go to first element in 'stack'
    # Visit adjacent nodes that are not in 'visited'
    # Add visited node to 'visited'
    # And visit its adjacent nodes

    node = problem.getStartState()

    visited = util.Stack()

    # Manually visit the starting node
    visited.push((node, None)) # Make sure that the start location will be selected by the algorithm (and not just one value of the location)

    # Execute the recursive algorithm for each successor of start
    for successor in problem.getSuccessors(node):
        nextDFS(problem, successor, visited)

    # Create a list of directions from the visited node list
    directions = [dir[1] for dir in visited.list[1::]] # Take the second element of all tuples (ignoring the starting position as it does not have a direction)
    print(directions)   # Print all directions
    return directions   # Return the directions

def nextDFS(problem, node, visited):

    # Add the node that's being visited to the list
    visited.push(node)

    if problem.isGoalState(node[0]):
        return visited

    # Iterate over all successors of this node
    for node in problem.getSuccessors(node[0]):
        # Make sure this successor has not been visited yet
        visitedLocations = [location[0] for location in visited.list]
        if node[0] not in visitedLocations:                         # Check for each successor that they haven't been visited yet
            done = nextDFS(problem, node, visited)                  # For each unvisited successor: execute the recursive algorithm
            if done is not None:                                    # If a goal has been reached, just return and don't check other successors
                return done

    visited.pop()   # Remove the node that should not be visited
    return None


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    done = None
    node = problem.getStartState()
    print(problem.getSuccessors(node))
    queue = []
    visited = util.Stack()

    queue.append(node)
    visited.push((node, None))

    while queue or done:
        node = queue.pop(0)
        print(node)
        if problem.isGoalState(node):
            done = True
        for successor in problem.getSuccessors(node):
            visitedLocations = [location[0] for location in visited.list]
            if node[0] not in visitedLocations:
                queue.append(successor)
                visited.push(successor)

    directions = [dir[1] for dir in visited.list[1::]]
    print(directions)
    return directions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
