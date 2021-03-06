# Reasons for Modeling: Extrapolation

# Another common use of modeling extrapolation to estimate data values 
# "outside" or "beyond" the range (min and max values of time) of the 
# measured data. In this exercise, we have measured distances for times 
# 0 through 5 hours, but we are interested in estimating how far we'd go 
# in 8 hours. Using the same data set from the previous exercise, we 
# have prepared a linear model distance = model(time). Use that model() 
# to make a prediction about the distance traveled for a time much larger than the other times in the measurements.

# [context figure]

# Instructions

# Use distance = model(time) to extrapolate beyond the measured data to 
# time=8 hours.
# Print the distance predicted and then check whether it is less than or 
# equal to 400.
# If your car can travel, at most, 400 miles on a full tank, and it takes 
# 8 hours to drive home, will you make it without refilling? You should 
# have answer=True if you'll make it, or answer=False if you will run out 
# of gas.

# Select a time not measured.
time = 8

# Use the model to compute a predicted distance for that time.
distance = model(time)

# Inspect the value of the predicted distance traveled.
print(distance)

# Determine if you will make it without refueling.
answer = (True <= 400)
print(answer)

time, distance
 0.0,     0.00
 1.0,    44.05
 2.0,   107.16
 3.0,   148.44
 4.0,   196.40
 5.0,   254.44
 6.0,   300.00

In [1]: # Select a time not measured.
        time = 8
        
        # Use the model to compute a predicted distance for that time.
        distance = model(time)
        
        # Inspect the value of the predicted distance traveled.
        print(distance)
        
        # Determine if you will make it without refueling.
        answer = (True <= 400)
        print(answer)
400
True

<script.py> output:
    400
    True