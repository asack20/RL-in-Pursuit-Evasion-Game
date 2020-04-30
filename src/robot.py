import numpy as np

class Robot:

    # Class Attribute
    # pose (x, y, orientation)
    # fov - field of view in radians
    # vel (forward vel, angular vel)
    # Map m
    SENSOR_NOISE_COEF = 0.1
    # Initializer / Instance Attributes
    # Sets initializes robot pose and properties
    def __init__(self, init_pose, fov):
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

    def senseRobot(self, other_pose):


        dist = np.sqrt(np.square(self.pose[0]-other_pose[0]) + np.square(self.pose[1]-other_pose[1]))
        ang =  np.arctan2(other_pose[1]-self.pose[1], other_pose[0]-self.pose[0])

        if np.abs(ang - self.pose[2]) <= self.fov/2:
            reading = np.round(dist + dist * np.random.default_rng().normal() * SENSOR_NOISE_COEF)


        return reading
#10 substeps
