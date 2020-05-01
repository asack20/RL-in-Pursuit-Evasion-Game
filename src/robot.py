import numpy as np
import random

class Robot:

    # Class Attribute
    # pose (x, y, orientation)
    # fov - field of view in radians
    SENSOR_NOISE_COEF = 0.1
    ANG_VEL_COEF = np.pi / 2
    LIN_VEL_COEF = 1
    # Initializer / Instance Attributes
    # Sets initializes robot pose and properties
    def __init__(self, init_pose, fov):
        self.pose = init_pose
        self.fov = fov

    # #Tries move and returns true if it is valid, Else, False
    # def tryMove(self, vel):
    #     pass

    # Moves
    # vel = [linear, rotation]
    def move(self, vel):
        new_x = self.pose[0] + vel[0] * np.cos(self.pose[2]) * self.LIN_VEL_COEF
        new_y = self.pose[1] + vel[0] * np.sin(self.pose[2]) * self.LIN_VEL_COEF
        new_or = self.pose[2] + vel[1] * self.ANG_VEL_COEF

        if vel[1] != 0:
            new_x = new_x + vel[0] * np.cos(new_or) * self.LIN_VEL_COEF
            new_y = new_y + vel[0] * np.sin(new_or) * self.LIN_VEL_COEF

        self.pose = (new_x, new_y, new_or)
        return self.pose
    #
    # #Sets Robot vel for moving
    #
    # def setVel(self, vel):
    #     self.vel = vel


    #returns cell indicies for where robot is located
    def inCell(self):
        return (self.pose[1]//1, self.pose[0]//1)

    def senseRobot(self, other_pose):
        dist = np.sqrt(np.square(self.pose[0]-other_pose[0]) + np.square(self.pose[1]-other_pose[1]))
        ang =  np.arctan2(other_pose[1]-self.pose[1], other_pose[0]-self.pose[0])

        if np.abs(ang - self.pose[2]) > self.fov/2:
            return 6

        reading = np.round(dist + dist * random.gauss(0,1) * self.SENSOR_NOISE_COEF)
        if reading < 0:
            reading = 0
        if reading > 5:
            reading = 6
        return reading
#10 substeps
