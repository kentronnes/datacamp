Writing an iterator to load data in chunks (1)
Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain length, say, 100. For example, with the pandas package (imported as pd), you can do pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next() on it.

In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World Bank Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator for numerous countries and years.

INSTRUCTIONS
100 XP
Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader.
Print the first two chunks from df_reader.

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))


                                 CountryName CountryCode  \
0                                 Arab World         ARB   
1                     Caribbean small states         CSS   
2             Central Europe and the Baltics         CEB   
3    East Asia & Pacific (all income levels)         EAS   
4      East Asia & Pacific (developing only)         EAP   
5                                  Euro area         EMU   
6  Europe & Central Asia (all income levels)         ECS   
7    Europe & Central Asia (developing only)         ECA   
8                             European Union         EUU   
9   Fragile and conflict affected situations         FCS   

                   IndicatorName      IndicatorCode  Year      Value  
0  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.285384  
1  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.597490  
2  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.507921  
3  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  22.471132  
4  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  16.917679  
5  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.096947  
6  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  55.378977  
7  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  38.066129  
8  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  61.212898  
9  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  17.891972  
                                      CountryName CountryCode  \
10         Heavily indebted poor countries (HIPC)         HPC   
11                                    High income         HIC   
12                           High income: nonOECD         NOC   
13                              High income: OECD         OEC   
14  Latin America & Caribbean (all income levels)         LCN   
15    Latin America & Caribbean (developing only)         LAC   
16   Least developed countries: UN classification         LDC   
17                            Low & middle income         LMY   
18                                     Low income         LIC   
19                            Lower middle income         LMC   

                    IndicatorName      IndicatorCode  Year      Value  
10  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  12.236046  
11  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.680332  
12  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  56.107863  
13  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  64.285435  
14  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  49.284688  
15  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.863308  
16  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960   9.616261  
17  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  21.272894  
18  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  11.498396  
19  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  19.810513