import numpy as np
from robot import Robot

class Map:

    # Class Attribute
    grid_sz = (10, 10)
    #grid
    #r_p # pursuer robot object
    #r_e # evader robot object

    # Initializer / Instance Attributes
    # Creates grid
    def __init__(self):
        self.grid = np.zeros(self.grid_sz)
        for i in range(self.grid_sz[0]//10):
            for j in range(self.grid_sz[1]//10):
                self.grid[(i*10):(i*10)+5, (j*10):(j*10)+5] = np.ones((5,5))

        self.r_p = Robot((0,0,0), np.pi/2)
        self.r_e = Robot((0,0,0), np.pi/2)

    # Checks if input is in an open space in Map
    def validSpace(self, pose):
        x_pos = pose[0]//1
        y_pos = pose[1]//1

        if x_pos < 0 or x_pos >= self.grid_sz[0] or y_pos < 0 or y_pose >= self.grid_sz[1]:
            return False
        elif self.grid[x_pos, y_pos] == 1:
            return False
        else:
            return True

    def pursuerScanner(self):
        return self.r_p.senseRobot(self.r_e.pose)

    def evaderScanner(self):
        return self.r_e.senseRobot(self.r_p.pose)

    def haveCollided(self):
        dist = np.sqrt(np.square(self.r_p.pose[0]-self.r_e.pose[0]) + np.square(self.r_p.pose[1]-self.r_e.pose[1]))
        if dist <= 1:
            return True
        else:
            return False

    def checkForObstacle(self, x, y):
        x = int(x)
        y = int(y)

        # check if the desired next state is out of bounds or a wall ( == 1)
        if y > self.grid.shape[0] - 1 or y < 0 or x > self.grid.shape[0] - 1 or x < 0:
            # return initial state if out of bounds
            return True
        elif self.grid[x, y] == 1:
            # return initial state if obstacle found
            return True
        else:
            # return next state if no obstacle found
            return False


    # Does nothing
    # Returns state of surrounding tiles (no robot)
    def getSurroundings(self, pose):
        # 0  open, 1 wall/outofbounds, 2 Robot
        # List (Up, down, left, right)
        x_pos = pose[0]//1
        y_pos = pose[1]//1

        surrounding = []
        #up (i-1, j)
        if x_pos-1 < 0 or self.grid[x_pos-1,y_pos] == 1:
            surrounding[0] = 1
        else:
            surrounding[0] = 0

        #down (i+1, j)
        if x_pos+1 >= self.grid_sz[0] or self.grid[x_pos+1,y_pos] == 1:
            surrounding[1] = 1
        else:
            surrounding[1] = 0

        #left (i, j-1)
        if y_pos-1 < 0 or self.grid[x_pos,y_pos-1] == 1:
            surrounding[2] = 1
        else:
            surrounding[2] = 0

        #right (i, j+1)
        if y_pos+1 >= self.grid_sz[1] or self.grid[x_pos,y_pos+1] == 1:
            surrounding[3] = 1
        else:
            surrounding[3] = 0

        return surrounding
