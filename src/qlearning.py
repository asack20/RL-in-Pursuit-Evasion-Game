# Source for Q-learning implementation: https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2
# Source for cutom Environment Creation: https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e

import gym
import numpy as np
import map
from gym import spaces, error, utils
from gym.utils import seeding
from environmentPlot import EnvironmentPlot

ACTION_LIST = ["forward", "backward", "turn_left", "turn_right", "stop", "turn_and_move_right", "turn_and_move_right"]
#[stop, turn left, turn right, forward, forward left, forwards right]
#linear vel = [0,1]
#angular ve = [-1, 0, 1]
N_DISCRETE_ACTIONS = len(ACTION_LIST)

#
Z_LIST = ["n", "e", "s", "w"]
N_DISCRETE_Z = len(Z_LIST)

HEIGHT = 100
WIDTH = 100
THETA = 4

class TurtleBotTag(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}


    def __init__(self, map=None):
        super(TurtleBotTag, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects

        # Obtain current map for training
        self.current_map = map.Map

        # Get map bounds
        self.height = self.current_map.grid_sz[0]
        self.width = self.current_map.grid_sz[1]
        self.theta = THETA

        # Establish Discrete Actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

        # Establish Observation Space: ADD ROBOT POSE
        self.observation_space = spaces.Box(low=0, high=N_DISCRETE_Z, shape =
                                    (HEIGHT, WIDTH, THETA), dtype_np.uint8)
        #self.observation_space = spaces.Box(low=0, high=width, shape=
        #                (HEIGHT, WIDTH), dtype=np.uint8)

        # Reset Initial Conditions
        self.reset()

    def step(self, action):
        # Execute one time step within the environment
        # pursuer and evader sense and then move
        # update the map with their pose
        pass

    def reset(self):
        # Reset the state of the environment to an initial state
        # reset to random robot starting positions so we can make sure they
        # all converge to the same solution
        self.pursuer_state = self.generate_random_pos() # numpy random (x, y, theta)
        self.evader_state = self.generate_random_pos() # numpy random (x, y, theta)
        self.pursuer_observation = self.get_observation(self.current_map, self.pursuer_state, self. evader_state)
        self.evader_observation = self.get_obeservation(self.current_map, self.pursuer_state, self. evader_state)

    def checkForObstacle(arg):
        pass

    def generate_random_pos(arg):
        heightRange = range(self.width)
        widthRange = range(self.width)
        thetaRange = range(self.theta)


        possiblePos = filter(checkForObstacle, zip(heightRange, widthRange))

        while True:
            # randomize position
            x = np.random.choice(widthRange, 1)
            y = np.random.choice(heightRange, 1)

            if checkForObstacle(x, y):
                theta = np.random.choice(thetaRange, 1)
                break

        return (x, y, theta)

    def checkForObstacle(x, y):
        return True


    def render(self, mode='human', close=False, **kwargs):
        # Render the environment to the screen
        self.visualization = environmentPlot(self.df, title="Test")

        if self.current_step > LOOKBACK_WINDOW_SIZE:
            self.visualization.render(self.current_step, self.net_worth,
            self.trades, window_size=LOOKBACK_WINDOW_SIZE)
        draw_screen()
