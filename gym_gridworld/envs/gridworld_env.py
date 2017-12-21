import gym_gridworld
from gym import Env
from gym import error, spaces

'''
ENVIRONMENT
--------------------------
|     |     |      |     |
|     |     |      | +1  |
|     |     |      |     |
--------------------------
|     |xxxxx|      |     |
|     |xxxxx|      | -1  |
|     |xxxxx|      |     |
--------------------------
|     |     |      |     |
|  S  |     |      |     |
|     |     |      |     |
--------------------------
This is the simple gridworld environment from the Russel and Norvig text

OBSERVATION:
(x,y) coordinates

ACTIONS:
 (1) NORTH
 (2) EAST
 (3) SOUTH
 (4) WEST

REWARD
 +1  (4,3)
 -1  (4,2)
  0  everywhere else

START STATE
(1,1)

EPISODE TERMINATION
(4,3)
(4,2)
 
'''

WIDTH = 4
HEIGHT = 3

class FooEnv(Env):
    metadata = {'render.modes':['human']}

    def __init__(self):
        self.grid = [[' ',' ',' ', +1]
                     [' ','#',' ', -1]
                     ['S',' ',' ',' ']]
        self.valid_states = ((1,1) , (1,2) , (1,3) , (2,1) , (2,3) , (3,1) , (3,2) , (3,3), (4,1) , (4,2) , (4,3))
        self.action_space = spaces.Box( 1 , 2 , 3 , 4 )
        self.observation_space = spaces.Box((1,1) , (1,2) , (1,3) , (2,1) , (2,2) , (2,3) , (3,1) , (3,2) , (3,3), (4,1) , (4,2) , (4,3))

    def _step(self, action):
        self.last_action = action
        x , y  = self.state
        if action == 1:
            y += 1
        elif action == 2:
            x += 1
        elif action == 3:
            y -= 1
        elif action == 4:
            x -= 1

        ##Update the state only if action has moved agent into a valid state
        if (x,y) in self.valid_states:
            self.state = (x,y)
        
        reward = 0
        done = False
        if self.state == (4,3):
            reward = 1
            done = True
        elif self.state == (4,2):
            reward = -1
            done = True
        
        return self._get_obs(), reward, done, {} 
    
    def _reset(self):
        self.state = (1,1)
        self.last_action = None
        return self._get_obs()

    def _get_obs(self):
        return self.state

    def _render(self, mode='human', close = False):
        print self.state