# Renaming Columns

# See how easy that was? You tidied up your dataset with a single 
# command! Now we just need a bit more fine-tuning. Change the column 
# names with pandas' rename function. Its syntax is df.rename(columns 
# = d, inplace = False), where d is a dictionary where the keys are 
# the columns you want to change, and the values are the new names 
# for these columns. The code inplace = False means the result would 
# be stored in a new DataFrame instead of the original one.

# Rename the variable column of df2_melted to Year and the value 
# column to Income.

# Click "Submit Answer" to print out the new tidy DataFrame.

# Import pandas
import pandas as pd

# Rename the columns of df2_melted: df2_tidy
df2_tidy = df2_melted.rename(columns = {'variable':'Year', 'value':'Income'}, inplace = False)

# Print out df2_tidy
print(df2_tidy)

In [1]: # Import pandas
        import pandas as pd
        
        # Rename the columns of df2_melted: df2_tidy
        df2_tidy = df2_melted.rename(columns = {'variable':'Year', 'value':'Income'}, inplace = False)
        
        # Print out df2_tidy
        print(df2_tidy)
        Country   Year    Income
0   Afghanistan  Y1980  21.48678
1       Albania  Y1980  25.22533
2       Algeria  Y1980  22.25703
3   Afghanistan  Y1981  21.46552
4       Albania  Y1981  25.23981
5       Algeria  Y1981  22.34745
6   Afghanistan  Y1982  21.45145
7       Albania  Y1982  25.25636
8       Algeria  Y1982  22.43647
9   Afghanistan  Y1983  21.43822
10      Albania  Y1983  25.27176
11      Algeria  Y1983  22.52105