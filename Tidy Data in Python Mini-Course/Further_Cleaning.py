# Further Cleaning

# What did you notice in the last exercise? While the three columns 
# melt into one, the dataset still has some problems. First of all, 
# when we know Elizabeth has brown eyes, it's redundant to record 
# that she doesn't have blue or black eyes. Therefore, what we want 
# to do is to get rid of all rows whose value in the value column is 
3 0. It is very easy to do this in pandas using the following command:

# df1 = df2[df2.column == value]

# where column is the name of the column we are examining and value 
# is the value we want to keep. This step will give us one row for 
# each girl that tells us only her correct eye color. Now the value 
# column is no longer necessary, so let's delete it:

# df.drop(lst, axis = 1)

# Here lst is a list of the columns we want to get rid of, and axis = 
# 1 specifies that we want to drop columns instead of rows.

# Instructions

# Filter the dataset to keep only the rows where value is 1.

# Delete the value column.

# Import pandas
import pandas as pd

# Melt the Black, Blue, and Brown columns of eyes: eyes_melted
eyes_melted = pd.melt(eyes, id_vars=['Name','Wear_Glasses'])
        
# Rename the variable column and save to eyes_renamed
 eyes_renamed = eyes_melted.rename(columns = {'variable':'Eye_Color'})

# Filter eyes_ranamed and save to eyes_filtered 
eyes_filtered = eyes_filtered = eyes_renamed[eyes_renamed.value == 1]

# Delete the `value` column and save to eyes_tidy
eyes_tidy = eyes_tidy = eyes_filtered.drop(['value'], axis = 1)

# print eyes_tidy
print(eyes_tidy)


# 1
        Name  Brown  Blue  Black Wear_Glasses
0     Esther      0     1      0        False
1  Elizabeth      1     0      0        False
2   Michelle      0     0      1         True

# 2
        Name Wear_Glasses Eye_Color  value
1  Elizabeth        False     Brown      1
3     Esther        False      Blue      1
8   Michelle         True     Black      1

# 3
        Name Wear_Glasses Eye_Color
1  Elizabeth        False     Brown
3     Esther        False      Blue
8   Michelle         True     Black