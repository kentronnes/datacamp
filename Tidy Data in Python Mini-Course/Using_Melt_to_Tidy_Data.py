# Using Melt to Tidy Data

# In df2, the years 1980, 1981, 1982, and 1983 mark the years when 
# BMI is observed. Thus, they represent three different observations 
# and should be seperated in three rows. A great tool to achieve this 
# is the melt function in the pandas package. Its basic syntax is 
# pd.melt(df, id_vars = lst), where df is the name of the dataframe 
# we're dealing with and lst is a list of all the columns that we want 
# to keep as columns. All the other columns will be "melted" together 
# in different rows. To get a more concrete idea, try melt yourself to 
# tidy the dataset df2!

# Instructions

# Import pandas using the alias pd.

# Melt df2! We want to maintain the Country column and melt all the 
# rest.

# Click "Submit" to print out the new melted DataFrame.

In [1]: df2
Out[1]: 
       Country     Y1980     Y1981     Y1982     Y1983
0  Afghanistan  21.48678  21.46552  21.45145  21.43822
1      Albania  25.22533  25.23981  25.25636  25.27176
2      Algeria  22.25703  22.34745  22.43647  22.52105


# Import pandas as pd
import pandas as pd

# Melt df2 into new dataframe: df2_melted
df2_melted = pd.melt(df2, id_vars=['Country'])

# print df2_melted
print(df2_melted)


In [2]: # Import pandas as pd
        import pandas as pd
        
        # Melt df2 into new dataframe: df2_melted
        df2_melted = pd.melt(df2, id_vars = ['Country'])
        
        # print df2_melted
        print(df2_melted)
        Country variable     value
0   Afghanistan    Y1980  21.48678
1       Albania    Y1980  25.22533
2       Algeria    Y1980  22.25703
3   Afghanistan    Y1981  21.46552
4       Albania    Y1981  25.23981
5       Algeria    Y1981  22.34745
6   Afghanistan    Y1982  21.45145
7       Albania    Y1982  25.25636
8       Algeria    Y1982  22.43647
9   Afghanistan    Y1983  21.43822
10      Albania    Y1983  25.27176
11      Algeria    Y1983  22.52105


