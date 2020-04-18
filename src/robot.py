import numpy as np
from map import Map

class Robot:

    # Class Attribute
    # pose (x, y, orientation)
    # fov - field of view in radians
    # vel (forward vel, angular vel)
    # Map m

    # Initializer / Instance Attributes
    # Sets initializes robot pose and properties
    def __init__(self, m, init_pose, fov):
        self.m = m
        self.pose = init_pose
        self.fov = fov

    #Tries move and returns true if it is valid, Else, False
    def tryMove(self, vel):
        pass

    # Moves
    def move(self):
        new_or = self.pose[2] + self.vel[1]
        new_x = self.pose[0] + self.vel[0] * np.cos(new_or)
        new_y = self.pose[1] + self.vel[0] * np.sin(new_or)
        self.pose = (new_x, new_y, new_or)

    #Sets Robot vel for moving
    def setVel(self, vel):
        self.vel = vel


    #returns cell indicies for where robot is located
    def inCell(self):
        return (self.pose[0]//1, self.pose[1]//1)
