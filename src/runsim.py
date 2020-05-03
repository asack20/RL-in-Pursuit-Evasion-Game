
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
    Q_p = np.zeros(env.Q_dim)
    Q_e = np.zeros(env.Q_dim)

    # 2. Parameters of Q-leanring
    eta = .628
    gma = .9
    step_num = 999
    epis = 5000
    rev_list = [] # rewards per episode calculate

    # 3. Q-learning Algorithm
    for i in range(epis):
        # Reset environment
        s_p, s_e = env.reset()
        rAll = 0
        d = False
        j = 0

        # The Q-Table learning algorithm
        while j < step_num:
            env.render()
            j+=1

            # Choose action from Q table
            a_p = np.argmax(Q_p[s_p] + np.random.randn(1, env.action_space.n)*(1./(i+1)))
            a_e = np.argmax(Q_e[s_e] + np.random.randn(1, env.action_space.n)*(1./(i+1)))

            #qprint("action selected:" + str(a))
            #Get new state & reward from environment
            s1_p, s1_e, r_p, r_e, d = env.step(a_p, a_e)
            #print("s1" + str(s1))
            #print("Q shape" + str(Q.shape))

            # Update Q-Table with new knowledge
            Q_p[s_p][a_p] = Q_p[s_p][a_p] + eta*(r_p + gma*np.max(Q_p[s1_p]) - Q_p[s_p][a_p])
            Q_e[s_e][a_e] = Q_e[s_e][a_e] + eta*(r_e + gma*np.max(Q_e[s1_e]) - Q_e[s_e][a_e])

            rAll += r_p + r_e
            s_p = s1_p
            s_e = s1_e

            if d == True:
                break
        rev_list.append(rAll)
        env.render()

    print("Reward Sum on all episodes " + str(sum(rev_list)/epis))
    print("Final Values Q-Table")
    print(Q)

if __name__ == '__main__':
    main()
