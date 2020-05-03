# Source for Q-learning implementation: https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2
# Source for cutom Environment Creation: https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e

import gym
import numpy as np
from map import Map
from robot import Robot
import matplotlib.pyplot as plt
from gym import spaces, error, utils
from gym.utils import seeding
import time

# linear vel = [0, 1]
# angular vel = [-1, 0, 1]
ACTION_LIST_NAMES = ["stop", "forward", "turn_left", "turn_right", "turn_and_move_left", "turn_and_move_right"]
ACTION_LIST = [(0, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]
N_DISCRETE_ACTIONS = len(ACTION_LIST)

Z_LIST = [0, 1, 2, 3, 4, 5, 6]
N_DISCRETE_Z = len(Z_LIST)

HEIGHT = 100
WIDTH = 100
THETA = 4
THETALIST = [0, np.pi/2, np.pi, 3/2*np.pi]


class TurtleBotTag(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(TurtleBotTag, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.fig = plt.figure()
        self.ax = self.fig.axes

        # Obtain current map for training
        self.map = Map()
        self.current_grid = self.map.grid

        # Get map bounds
        self.height = self.map.grid_sz[0]
        self.width = self.map.grid_sz[1]
        self.theta = THETA
        self.observations = N_DISCRETE_Z

        # Establish Discrete Actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

        # Establish Observation Space: ADD ROBOT POSE
        self.observation_space = spaces.Box(low=0, high=1, shape=
        (self.height, self.width, self.theta, self.observations), dtype=np.uint8)
        self.Q_dim = (self.height, self.width, self.theta, self.observations, self.action_space.n)

        # self.observation_space = spaces.Box(low=0, high=width, shape=
        #                (HEIGHT, WIDTH), dtype=np.uint8)

        # Reset Initial Conditions
        self.reset()

    def step(self, p_action, e_action):
        # Execute one time step within the environment
        # pursuer and evader sense and then move
        # update the map with their pose

        # MOVE ROBOTS
        p_vel = ACTION_LIST[p_action]
        e_vel = ACTION_LIST[e_action]
        #print("PURSUER action taken: ", ACTION_LIST_NAMES[p_action], ". velocities", p_vel)
        #print("EVADER action taken: ", ACTION_LIST_NAMES[e_action])

        p_pose = self.map.r_p.move([p_vel[0], p_vel[1]], self.map)
        e_pose = self.map.r_e.move([e_vel[0], e_vel[1]], self.map)
        #print("PURSUER new pose: ", p_pose)
        #print("EVADER new pose: ", e_pose)

        p_observation = self.map.senseEvader()
        e_observation = self.map.sensePursuer()

        # print("e_observation " + str(p_observation))

        p_state = tuple([int(x) for x in np.array([p_pose[0], p_pose[1], p_pose[2], p_observation])])
        e_state = tuple([int(x) for x in np.array([e_pose[0], e_pose[1], e_pose[2], e_observation])])

        done = self.map.haveCollided()

        if done == True:
            p_reward = 100
            e_reward = -100
        else:
            p_reward = -1
            e_reward = 1

        return p_state, e_state, p_reward, e_reward, done

    def reset(self):
        # Reset the state of the environment to an initial state
        # reset to random robot starting positions so we can make sure they
        # all converge to the same solution
        self.map.r_p.pose = self.generateRandomPos()  # numpy random (x, y, theta)
        self.map.r_e.pose = self.generateRandomPos()  # numpy random (x, y, theta)
        self.p_observation = self.map.senseEvader()
        self.e_observation = self.map.sensePursuer()

        p_pose = self.map.r_p.pose
        e_pose = self.map.r_e.pose

        p_observation = self.map.senseEvader()
        e_observation = self.map.sensePursuer()

        p_state = tuple([int(x) for x in np.array([p_pose[0], p_pose[1], p_pose[2], p_observation])])
        e_state = tuple([int(x) for x in np.array([e_pose[0], e_pose[1], e_pose[2], e_observation])])

        return p_state, e_state

    # define states as state =  (y, x, theta)

    def generateRandomPos(self):
        heightRange = range(self.width)
        widthRange = range(self.width)
        thetaRange = range(self.theta)

        while True:
            # randomize position
            x = np.random.choice(widthRange)
            y = np.random.choice(heightRange)

            if not self.map.checkForObstacle(x, y):
                theta = np.random.choice(thetaRange)
                break

        return (x, y, theta)

    def render(self):
        # Render the environment to the screen
        plt.cla()
        plt.imshow(self.map.grid, origin='lower')
        plt.plot(self.map.r_p.pose[0], self.map.r_p.pose[1], 'bo', label='Pursuer')
        plt.plot(self.map.r_e.pose[0], self.map.r_e.pose[1], 'ro', label='Evader')
        plt.legend(loc='lower left')
        # Show the graph without blocking the rest of the program

        plt.draw()
        plt.pause(0.005)
