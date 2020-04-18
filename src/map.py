import numpy as np


class Map:

    # Class Attribute
    grid_sz = (80, 30)

    # Initializer / Instance Attributes
    def __init__(self):
        self.grid = np.zeros(self.grid_sz)
