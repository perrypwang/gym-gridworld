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
 (0) NORTH
 (1) EAST
 (2) SOUTH
 (3) WEST

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

class GridworldEnv(Env):
    metadata = {'render.modes':['human']}

    def __init__(self):
        self.state = (0,0)
        self.valid_states = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2), (3,0), (3,1), (3,2)]
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple((spaces.Discrete(4), spaces.Discrete(3)))
        self.reward_range = (-1,1)

    def _step(self, action):
        self.last_action = action
        x , y  = self.state
        if action == 0:
            y += 1
        elif action == 1:
            x += 1
        elif action == 2:
            y -= 1
        elif action == 3:
            x -= 1

        ##Update the state only if action has moved agent into a valid state
        if (x,y) in self.valid_states:
            self.state = (x,y)
        
        reward = 0
        done = False
        if self.state == (3,2):
            reward = 1
            done = True
        elif self.state == (3,1):
            reward = -1
            done = True
        
        return self._get_obs(), reward, done, {} 
    
    def _reset(self):
        self.state = (0,0)
        self.last_action = None
        return self._get_obs()

    def _get_obs(self):
        return self.state

    def _render(self, mode='human', close = False):
        print(self._get_obs())