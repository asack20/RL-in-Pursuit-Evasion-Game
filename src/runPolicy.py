
import numpy as np
import matplotlib.pyplot as plt
import gym
from map import Map
from robot import Robot
from qlearning import TurtleBotTag
import datetime
import os

def main():

    samples = 100
    iterations = 100

    # 1. Load Environment and Q-table structure
    env = TurtleBotTag()

    parent_dir = os.getcwd()
    directory1 = "../results/"
    dir_name = os.path.join(parent_dir, directory1)
    folder = '04_May_2020_05_12_00'
    Q_p = np.load(dir_name + folder + "/bestPolicyQTableP.npy")
    Q_e = np.load(dir_name + folder + "/bestPolicyQTableE.npy")

    # 2. Parameters of Q-leanring
    eta = .01
    gma = .9
    step_num = 250
    epis = 2
    rev_list_p = [] # rewards per episode calculate
    rev_list_e = [] # rewards per episode calculate
    steps_list = [] # steps per episode
    env.RENDER_FREQ = 1 # How often to render an episode
    env.RENDER_PLOTS = True # whether or not to render plots
    env.SAVE_PLOTS = True # Whether or not to save plots

    # 3. Q-learning Algorithm
    for i in range(epis):
        # Reset environment
        s_p, s_e = env.reset()
        rAll_p = 0
        rAll_e = 0
        d = False
        j = 0
        env.epis = i
        # The Q-Table learning algorithm
        while j < step_num:
            env.step_num = j
            env.render()
            j += 1

            # Choose best action from Q table
            a_p = np.argmax(Q_p[s_p])
            a_e = np.argmax(Q_e[s_e])

            s1_p, s1_e, r_p, r_e, d = env.step(a_p, a_e)

            rAll_p += r_p
            rAll_e += r_e
            s_p = s1_p
            s_e = s1_e

            if d == True:
                break

        rev_list_p.append(rAll_p)
        rev_list_e.append(rAll_p)
        steps_list.append(j)
        env.render()

    print("Pursuer Reward Sum on all episodes " + str(sum(rev_list_p)/epis))
    print("Evader Reward Sum on all episodes " + str(sum(rev_list_e)/epis))
    print("Pursuer Final Values Q-Table:\n", Q_p)
    print("Evader Final Values Q-Table:\n", Q_e)

    fname = env.dir_name
    fP = open(fname + "bestPolicyStats.txt", "w+")
    fP.write('Running Policy From: ' + folder + "\n" )
    fP.write("Pursuer Final Values Q-Table:\n")
    fP.write("eta = " + str(eta) + "\n")
    fP.write("gma = " + str(gma) + "\n")
    fP.write("step_num = " + str(step_num) + "\n")
    fP.write("epis = " + str(epis) + "\n")
    fP.close()

    np.savetxt(fname + "RevListP.txt", rev_list_p)
    np.savetxt(fname + "RevListE.txt", rev_list_e)
    np.savetxt(fname + "StepsList.txt", steps_list)

    '''
    fname = env.dir_name
    fP = open(fname + "bestPolicyStats.txt","w+")
    fP.write("Pursuer Final Values Q-Table:\n")
    fP.write("eta = " + str(eta) + "\n")
    fP.write("gma = " + str(gma) + "\n" )
    fP.write("step_num = " + str(step_num) + "\n")
    fP.write("epis = " + str(epis) + "\n")
    fP.close()

    np.save(fname + "bestPolicyQTableP", Q_p)
    np.save(fname + "bestPolicyQTableE", Q_e)
    np.savetxt(fname + "RevListP", rev_list_p)
    np.savetxt(fname + "RevListE", rev_list_e)
    np.savetxt(fname + "StepsList", steps_list)
    '''

if __name__ == '__main__':
    main()
