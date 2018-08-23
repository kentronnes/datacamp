# Calculate the odds

# The histogram of the previous exercise was created
# from a Numpy array ends, that contains 500 integers.
# Each integer represents the end point of a random walk.
# To calculate the chance that this end point is greater
# than or equal to 60, you can count the number of integers
# in ends that are greater than or equal to 60 and divide
# that number by 500, the total number of simulations.

# Well then, what's the estimated chance that you'll reach
# 60 steps high if you play this Empire State Building game?
# The ends array is everything you need; it's available in
# your Python session so you can make calculations in the
# IPython Shell.

# INSTRUCTIONS

# Possible Answers

# 48.8%
# 73.9%
# 78.4%
# 95.9%

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 500 times
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Calculate values in ends[-1] that are greater than 60
print(np.count_nonzero(ends >= 60)/len(ends))
