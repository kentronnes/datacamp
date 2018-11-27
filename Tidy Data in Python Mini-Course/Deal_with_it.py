# Deal with it!

# In the previous exercise, the three columns--Black, Blue, and 
# Brown--represent the same variable: eye color. It would make much 
# more sense to merge them into one column. Use melt to do it!

# Instructions

# Use melt to leave Name and Wear_Glasses intact and combine 
# everything else.

# Rename the variable column to Eye_Color.

# Hit "Submit Answer" to print out the resulting dataframe.



# Import pandas
import pandas as pd

# Melt the Black, Blue, and Brown columns of eyes: eyes_melted
eyes_melted = pd.melt(eyes, id_vars=['Name','Wear_Glasses'])

# Rename the variable column and save to eyes_renamed
eyes_renamed = eyes_melted.rename(columns = {'variable':'Eye_Color'})

# print out eyes_renamed
print(eyes_renamed)

In [1]: eyes
Out[1]: 
        Name  Brown  Blue  Black Wear_Glasses
0     Esther      0     1      0        False
1  Elizabeth      1     0      0        False
2   Michelle      0     0      1         True

In [2]: # Import pandas
        import pandas as pd
        
        # Melt the Black, Blue, and Brown columns of eyes: eyes_melted
        eyes_melted = pd.melt(eyes, id_vars=['Name','Wear_Glasses'])
        
        # Rename the variable column and save to eyes_renamed
        eyes_renamed = eyes_melted.rename(columns = {'variable':'Eye_Color'})
        
        # print out eyes_renamed
        print(eyes_renamed)
        Name Wear_Glasses Eye_Color  value
0     Esther        False     Brown      0
1  Elizabeth        False     Brown      1
2   Michelle         True     Brown      0
3     Esther        False      Blue      1
4  Elizabeth        False      Blue      0
5   Michelle         True      Blue      0
6     Esther        False     Black      0
7  Elizabeth        False     Black      0
8   Michelle         True     Black      1

