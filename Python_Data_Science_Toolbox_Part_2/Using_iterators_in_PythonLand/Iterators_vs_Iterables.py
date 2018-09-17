# Iterators vs Iterables
# Let's do a quick recall of what you've learned about iterables 
# and iterators. Recall from the video that an iterable is an 
# object that can return an iterator, while an iterator is an 
# object that keeps state and produces the next value when you 
# call next() on it. In this exercise, you will identify which 
# object is an iterable and which is an iterator.

# The environment has been pre-loaded with the variables flash1 
# and flash2. Try printing out their values with print() and 
# next() to figure out which is an iterable and which is an 
# iterator.

# INSTRUCTIONS

# Possible Answers

# Both flash1 and flash2 are iterators.

# Both flash1 and flash2 are iterables.

# flash1 is an iterable and flash2 is an iterator.

In [1]: print(flash1)
['jay garrick', 'barry allen', 'wally west', 'bart allen']

In [2]: next(flash1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(flash1)
TypeError: 'list' object is not an iterator

In [3]: it = iter(flash1)

In [4]: next(it)
Out[4]: 'jay garrick'

In [5]: print(flash2)
<list_iterator object at 0x7f236e8944e0>

In [6]: it2 = iter(flash2)

In [7]: next(it2)
Out[7]: 'jay garrick'

In [8]: next(it2)
Out[8]: 'barry allen'

In [9]: 

# Answer: flash1 is an iterable and flash2 is an iterator.
