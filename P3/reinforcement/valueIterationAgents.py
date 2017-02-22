# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # for all the states, calculate
        while self.iterations > 0:
          self.iterations = self.iterations -1
          tmpValue = util.Counter() # same as the values, we only change in the final the values
          for state in self.mdp.getStates():
            maxV = -9999999
            for action in self.mdp.getPossibleActions(state): #compute all the posible actions of the stats
              totalvalue = self.getQValue(state,action) #get the Qvalue of an state and a specific action
              maxV = max(totalvalue,maxV)
            if maxV == -9999999:
              maxV = 0
            tmpValue[state]=maxV #store the value in out temporal array of values
          self.values = tmpValue # asign in the final values the calculated values for this iteration

        #util.raiseNotDefined()


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #Formula of the sumatory for all the states extracted in Wikipedia for Markov Decision process
        value = 0
        for nextState , probNextSate in self.mdp.getTransitionStatesAndProbs(state,action):
          value +=  probNextSate * ( self.mdp.getReward(state,action,nextState) + (self.discount*self.getValue(nextState) ) ) 
        return value

       

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        value = -999999999999
        bestAction = None
        #we need to obtain the best policy,
        if self.mdp.isTerminal(state):
          return None
        for action in self.mdp.getPossibleActions(state): #for all the actions of a state
          qvalue = self.computeQValueFromValues(state,action) #calculate the Qvalue of an specific action
          if qvalue > value: #store the best qvale and the action that makes it
            bestAction = action
            value = qvalue
        return bestAction
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
