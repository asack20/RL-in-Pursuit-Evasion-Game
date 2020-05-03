import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
#import gym
#import datetime

rev_list_e = np.loadtxt("../results/03_May_2020_19_45_43RevListE")
rev_list_p = np.loadtxt("../results/03_May_2020_19_45_43RevListP")
steps_list = np.loadtxt("../results/03_May_2020_19_45_43StepsList")

rev_e_smooth = sig.medfilt(rev_list_e, kernel_size=101)
rev_p_smooth = sig.medfilt(rev_list_p, kernel_size=101)
steps_smooth = sig.medfilt(steps_list, kernel_size=101)

plt.figure()
plt.suptitle('Agent Rewards vs Episode')
plt.subplot(2,1,1)
plt.plot(rev_list_p, 'b.', label ="Pursuer")
plt.title('Pursuer')
plt.xlabel('Episode Number')
plt.ylabel('Reward Amount')

plt.subplot(2,1,2)
plt.plot(rev_list_e, 'r.', label ="Evader")
plt.title('Evader')
plt.xlabel('Episode Number')
plt.ylabel('Reward Amount')


plt.figure()
plt.suptitle('Agent Rewards vs Episode (Smooth)')
plt.subplot(2,1,1)
plt.plot(rev_p_smooth, 'b.', label ="Pursuer")
plt.title('Pursuer')
plt.xlabel('Episode Number')
plt.ylabel('Reward Amount')

plt.subplot(2,1,2)
plt.plot(rev_e_smooth, 'r.', label ="Evader")
plt.title('Evader')
plt.xlabel('Episode Number')
plt.ylabel('Reward Amount')

plt.figure()
plt.plot(steps_list, '.', label ="# of Steps")
plt.title('Number of Steps vs Episode')
plt.xlabel('Episode Number')
plt.ylabel('# of Steps')

plt.show()


plt.figure()
plt.plot(steps_smooth, '.', label ="# of Steps")
plt.title('Number of Steps vs Episode (Smooth)')
plt.xlabel('Episode Number')
plt.ylabel('# of Steps')

plt.show()

