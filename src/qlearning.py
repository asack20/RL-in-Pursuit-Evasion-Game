# Source for Q-learning implementation: https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2
# Source for cutom Environment Creation: https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e

import gym
import numpy as np
from gym import spaces
from environmentPlot import EnvironmentPlot

ACTION_LIST = ["forward", "backward", "turn_left", "turn_right", "stop", "turn_and_move_right", "turn_and_move_right"]
#[stop, turn left, turn right, forward, forward left, forwards right]
#linear vel = [0,1]
#anglar ve = [-1, 0, 1]
N_DISCRETE_ACTIONS = len(ACTION_LIST)

Z_LIST = ["nothing", "n_wall", "e_wall", "s_wall", "w_wall", "n_bot", "e_bot", "s_bot", "w_bot"]
N_DISCRETE_Z = len(Z_LIST)

HEIGHT = 100
WIDTH = 100

class TurtleBotTag(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, arg1, arg2, ...):
    super(TurtleBotTag, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects

    # Establish Discrete Actions:
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

    # Establish Observation Space: ADD ROBOT POSE
    self.observation_space = spaces.Box(low=0, heigh=N_DISCRETE_Z, shape =
                                    (HEIGHT, WIDTH), dtype_np.uint8)

    #self.observation_space = spaces.Box(low=0, high=width, shape=
    #                (HEIGHT, WIDTH), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    ...

  def reset(self):
    # Reset the state of the environment to an initial state
    ...

  def render(self, mode='human', close=False, **kwargs):
    # Render the environment to the screen
    self.visualization = environmentPlot(self.df, title="Test")

    if self.current_step > LOOKBACK_WINDOW_SIZE:
      self.visualization.render(self.current_step, self.net_worth,
        self.trades, window_size=LOOKBACK_WINDOW_SIZE)
    draw_screen()



# 0. Create instance of custom environment



# 1. Load Environment and Q-table structure
env = gym.make('FrozenLake8x8-v0')
Q = np.zeros([env.observation_space.n,env.action_space.n])
# env.obeservation.n, env.action_space.n gives number of states and action in env loaded

# 2. Parameters of Q-leanring
eta = .628
gma = .9
epis = 5000
rev_list = [] # rewards per episode calculate

# 3. Q-learning Algorithm
for i in range(epis):
    # Reset environment
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    #The Q-Table learning algorithm
    while j < 99:
        env.render()
        j+=1
        # Choose action from Q table
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        #Get new state & reward from environment
        s1,r,d,_ = env.step(a)
        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] + eta*(r + gma*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    rev_list.append(rAll)
    env.render()

print "Reward Sum on all episodes " + str(sum(rev_list)/epis)
print "Final Values Q-Table"
print Q
