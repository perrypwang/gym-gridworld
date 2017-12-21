# gym-gridworld
The Gridworld environment is a single agent domain featuring a discrete state and action space.

### ENVIRONMENT
```
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
```
This is the simple gridworld environment from the Russel and Norvig text

### OBSERVATION:
(x,y) coordinates

### ACTIONS:
 (1) NORTH
 (2) EAST
 (3) SOUTH
 (4) WEST

### REWARD
 +1  (4,3)
 -1  (4,2)
  0  everywhere else

### START STATE
(1,1)

### EPISODE TERMINATION
(4,3)
(4,2)

# Installation
```
cd gym-gridworld
pip install -e .
```