import numpy as np

class Map:

    # Class Attribute
    grid_sz = (40, 40)
    #grid

    # Initializer / Instance Attributes
    # Creates grid
    def __init__(self):
        self.grid = np.zeros(self.grid_sz)
        for i in range(self.grid_sz[0]//10):
            for j in range(self.grid_sz[1]//10):
                self.grid[(i*10):(i*10)+5, (j*10):(j*10)+5] = np.ones((5,5))

    # Checks if input is in an open space in Map
    def validSpace(self, pose)
        x_pos = pose[0]//1
        y_pos = pose[1]//1

        if x_pos < 0 or x_pos >= self.grid_sz[0] or y_pos < 0 or y_pose >= self.grid_sz[1]:
            return False
        elif self.grid[x_pos, y_pos] == 1:
            return False
        else:
            return True

    # Returns state of surrounding tiles (no robot)
    def getSurroundings(self, pose)
        # 0  open, 1 wall/outofbounds, 2 Robot
        # List (Up, down, left, right)
        x_pos = pose[0]//1
        y_pos = pose[1]//1

        surrounding = []
        #up (i-1, j)
        if x_pos-1 < 0 or self.grid[x_pos-1,y_pos] == 1
            surrounding[0] = 1
        else:
            surrounding[0] = 0

        #down (i+1, j)
        if x_pos+1 >= self.grid_sz[0] or self.grid[x_pos+1,y_pos] == 1
            surrounding[1] = 1
        else:
            surrounding[1] = 0

        #left (i, j-1)
        if y_pos-1 < 0 or self.grid[x_pos,y_pos-1] == 1
            surrounding[2] = 1
        else:
            surrounding[2] = 0

        #right (i, j+1)
        if y_pos+1 >= self.grid_sz[1] or self.grid[x_pos,y_pos+1] == 1
            surrounding[3] = 1
        else:
            surrounding[3] = 0

        return surrounding
