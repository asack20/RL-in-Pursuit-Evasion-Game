
import numpy as np
import matplotlib.pyplot as plt
import gym
from map import Map
from robot import Robot
from qlearning import TurtleBotTag
import datetime

def main():
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
    eta = .005
    gma = .9
    epsilon = 1.1
    step_num = 999
    epis = 200000
    rev_list_p = []  # rewards per episode calculate
    rev_list_e = []  # rewards per episode calculate
    steps_list = []  # steps per episode
    env.RENDER_FREQ = 50000  # How often to render an episode
    env.RENDER_PLOTS = True  # whether or not to render plots
    env.SAVE_PLOTS = True  # Whether or not to save plots

    # 3. Q-learning Algorithm
    for i in range(epis):
        # Reset environment
        s_p, s_e = env.reset()
        rAll_p = 0
        rAll_e = 0
        d = False
        j = 0
        if i != 0:
            epsilon = 1/np.floor(i/epis/20)
        env.epis = i
        # The Q-Table learning algorithm
        while j < step_num:
            env.step_num = j
            env.render()
            j += 1

            # Choose action from Q table based on epsilon-greedy
            if np.random.rand() > epsilon:
                a_p = np.argmax(Q_p[s_p])
                a_e = np.argmax(Q_e[s_e])
            else:
                a_p = np.random.randint(0, env.action_space.n)
                a_e = np.random.randint(0, env.action_space.n)


            #a_p = np.argmax(Q_p[s_p] + np.random.randn(1, env.action_space.n)*(epis/2./(i+1)))
            #a_e = np.argmax(Q_e[s_e] + np.random.randn(1, env.action_space.n)*(epis/2./(i+1)))

            #qprint("action selected:" + str(a))
            #Get new state & reward from environment
            s1_p, s1_e, r_p, r_e, d = env.step(a_p, a_e)
            #print("s1" + str(s1))
            #print("Q shape" + str(Q.shape))

            # Update Q-Table with new knowledge
            Q_p[s_p][a_p] = Q_p[s_p][a_p] + eta*(r_p + gma*np.max(Q_p[s1_p]) - Q_p[s_p][a_p])
            Q_e[s_e][a_e] = Q_e[s_e][a_e] + eta*(r_e + gma*np.max(Q_e[s1_e]) - Q_e[s_e][a_e])

            rAll_p += r_p
            rAll_e += r_e
            s_p = s1_p
            s_e = s1_e

            if d == True:
                break

        rev_list_p.append(rAll_p)
        rev_list_e.append(rAll_e)
        steps_list.append(j)
        env.render()

    print("Pursuer Reward Sum on all episodes " + str(sum(rev_list_p)/epis))
    print("Evader Reward Sum on all episodes " + str(sum(rev_list_e)/epis))
    print("Pursuer Final Values Q-Table:\n", Q_p)
    print("Evader Final Values Q-Table:\n", Q_e)

    fname = env.dir_name
    fP = open(fname + "/bestPolicyStats.txt","w+")
    fP.write("Pursuer Final Values Q-Table:\n")
    fP.write("eta = " + str(eta) + "\n")
    fP.write("gma = " + str(gma) + "\n" )
    fP.write("step_num = " + str(step_num) + "\n")
    fP.write("epis = " + str(epis) + "\n")
    fP.close()

    np.save(fname + "/bestPolicyQTableP", Q_p)
    np.save(fname + "/bestPolicyQTableE", Q_e)
    np.savetxt(fname + "/RevListP.txt", rev_list_p)
    np.savetxt(fname + "/RevListE.txt", rev_list_e)
    np.savetxt(fname + "/StepsList.txt", steps_list)


if __name__ == '__main__':
    main()
