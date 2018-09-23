# Turning this all into a DataFrame

# You've zipped lists together, created a function to house your 
# code, and even used the function in a list comprehension to 
# generate a list of dictionaries. That was a lot of work and you 
# did a great job!

# You will now use of all these to convert the list of dictionaries 
# into a pandas DataFrame. You will see how convenient it is to 
# generate a DataFrame from dictionaries with the DataFrame() 
# function from the pandas package.

# The lists2dict() function, feature_names list, and row_lists list 
# have been preloaded for this exercise.

# Go for it!

# INSTRUCTIONS

# To use the DataFrame() function you need, first import the pandas 
# package with the alias pd.

# Create a DataFrame from the list of dictionaries in list_of_dicts 
# by calling pd.DataFrame(). Assign the resulting DataFrame to df.

# Inspect the contents of df by printing the head of the DataFrame.

# Import the pandas package
import pandas as pd

# From previous exercise: Writing a function to help you			   
# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict		

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())    