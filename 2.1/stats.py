# Write a script called "stats.py" that prints the 
# mean, median, mode, range, variance, and standard deviation 
# for the Alcohol and Tobacco dataset with full text 
# (ex. "The range for the Alcohol and Tobacco dataset is ..."). 
# Push the code to Github and enter the link below.

import pandas as pd
import pdb

data = '''Region, Alcohol, Tobacco
	North, 6.47, 4.03
	Yorkshire, 6.13, 3.76
	Northeast, 6.19, 3.77
	East Midlands, 4.89, 3.34
	West Midlands, 5.63, 3.47
	East Anglia, 4.52, 2.92
	Southeast, 5.89, 3.20
	Southwest, 4.79, 2.71
	Wales, 5.27, 3.53
	Scotland, 6.08, 4.51
	Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#pdb.set_trace() #debugger

alcr = max(df['Alcohol']) - min(df['Alcohol'])

alcm = df['Alcohol'].mean()
alcs = df['Alcohol'].std()
alcv = df['Alcohol'].var()

tobr = max(df['Tobacco']) - min(df['Tobacco'])
tobm = df['Tobacco'].mean()
tobs = df['Tobacco'].std()
tobv = df['Tobacco'].var()

print "alcohol mean is ", alcm
print "alcohol range is ", alcr
print "alcohol standard deviation is ", alcs
print "alcohol variance is ", alcv

print "Tobacco mean is ", tobm
print "Tobacco range is ", tobr
print "Tobacco standard deviation is ", tobs
print "Tobacco variance is ", tobv
