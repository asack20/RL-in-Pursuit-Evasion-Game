# Script to analyze reward and number of steps from training

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# CHANGE:
dir = "../results/03_May_2020_21_50_40/"

rev_list_e = np.loadtxt(dir + "RevListE.txt")
rev_list_p = np.loadtxt(dir + "RevListP.txt")
steps_list = np.loadtxt(dir + "StepsList.txt")

kernel_list = [1, 9, 21, 51, 101]

for k in kernel_list:
    rev_e_smooth = sig.medfilt(rev_list_e, kernel_size=k)
    rev_p_smooth = sig.medfilt(rev_list_p, kernel_size=k)
    steps_smooth = sig.medfilt(steps_list, kernel_size=k)

    plt.figure()
    plt.suptitle('Agent Rewards vs Episode (Medfilt w %d kernel)' % k)
    plt.subplot(2, 1, 1)
    plt.plot(rev_p_smooth, 'b.', label="Pursuer")
    plt.title('Pursuer')
    plt.xlabel('Episode Number')
    plt.ylabel('Reward Amount')

    plt.subplot(2, 1, 2)
    plt.plot(rev_e_smooth, 'r.', label="Evader")
    plt.title('Evader')
    plt.xlabel('Episode Number')
    plt.ylabel('Reward Amount')

    plt.figure()
    plt.plot(steps_smooth, '.', label="# of Steps")
    plt.title('Number of Steps vs Episode (Medfilt w %d kernel)' % k)
    plt.xlabel('Episode Number')
    plt.ylabel('# of Steps')


plt.show()

