
import numpy as np
import matplotlib.pyplot as plt
import gym
from map import Map
from robot import Robot
from qlearning import TurtleBotTag

def main():
    # m = Map()

    # plt.imshow(m.grid)
    # plt.plot(m.r_p.pose[0], m.r_p.pose[1], 'bo', label='Pursuer')
    # plt.plot(m.r_e.pose[0], m.r_e.pose[1], 'ro', label='Evader')
    # plt.legend()
    # plt.show()

    samples = 100
    iterations = 100


    # 0. Create instance of custom environment

#reward
#pursuer
#done +100
# time -1
# see +5 (try with and without)

#evader
#done -100
#time +1
#see -5

    # 1. Load Environment and Q-table structure
    env = TurtleBotTag()
    Q = np.zeros(env.Q_dim)

    # 2. Parameters of Q-leanring
    eta = .628
    gma = .9
    epis = 5000
    rev_list = [] # rewards per episode calculate

    # 3. Q-learning Algorithm
    for i in range(epis):
        # Reset environment
        s, s_other = env.reset()

        rAll = 0
        d = False
        j = 0
        #The Q-Table learning algorithm
        while j < 99:
            env.render()
            j+=1
            # Choose action from Q table
            a = np.argmax(Q[s] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
            print(Q[s].shape)

            #Get new state & reward from environment
            s1, s2, r, r2, d = env.step(a)
            #Update Q-Table with new knowledge
            Q[s,a] = Q[s,a] + eta*(r + gma*np.max(Q[s1,:]) - Q[s,a])
            rAll += r
            s = s1
            if d == True:
                break
        rev_list.append(rAll)
        env.render()

    print ("Reward Sum on all episodes " + str(sum(rev_list)/epis))
    print ("Final Values Q-Table")
    print (Q)

if __name__ == '__main__':
    main()
