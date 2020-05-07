# Reinforcement Learning in Pursuit Evasion Game
Tufts Probabilistic Robotics Spring 2020 Final Project

# PursuitEvasionGame
Reinforcement Learning in Pursuit-Evasion Games tackles the classical problem of
the imperfect Pursuit-Evasion Game. One of the agents acts as the  
seeker, planning its movements and actions based on its observations of the  
environment. The evader attempts to find the optimal path away from the seeker
using its own observations and knowledge base.  

We use a Q-learning reinforcement learning algorithm to train adversarial models
to compete against each other in the same game.  The interface of our algorithm
is based off the OpenAI gym API, where we designed a custom environment for our
pursuit evasion game.  

We discretize our space into a grid structure with 4 potential orientations.  
We define our action space into 6 possible movements and our observation spaces
into 2 possible observations.  We used various sensor models to see which
sensing techniques provide the most useful and powerful information while training.

This is an important problem, as motion tracking and pursuit has many real-world
applications. Some common Pursuit-Evasion applications involve search and rescue
missions where the target could be unknowingly moving away from the seeker,
corralling of uncooperative livestock, tracking vehicles through road networks,
and human-follower assistive robots. Creating a generalized approach to the
Pursuit-Evasion existing technology can be used to perform many tasks previously
only able to completed by humans.

# Dependencies
python version >= 3.6
pip
numpy
gym
matplotlib


# How to run an example
# training
python runsim.py

# trained sample run
python runpolicy.py


# File Descriptions
* runsim.py: Runs the whole simulation and the iterations of the Q-Learning
  algorithm

* runpolicy.py: Runs the optimal policy of the specified Q-table hardcoded into
  the script.

* qlearning.py: Contains the Q-learning algorithm based off the OpenAI gym API
  interface.

* map.py:
  implements and contains the entire robotic environment encompassing the Map
  and both robots

* robot.py:
  Contains the attributes and functionality for a single robot agent.

* make_movies.py: produces video based on images produced in the results folder

* install_dependencies.sh: shell script for installing necessary python packages

architecture

classes:
