import pandas as pd

df = pd.read_csv('olympics.csv', skiprows=4)

# index object is immutable array
# indexing allows us to access a row or column using a label

print(df.index) # Output :  RangeIndex(start=0, stop=29216, step=1)

print(type(df.index))   # Output : <class 'pandas.core.indexes.range.RangeIndex'>

print (df.index[100])

# df.index[100] = 5 # typeError: immutable, cannot be changed


# set_index()
# method of dataframe which determines which series is going to be index
# inplace = False by default

# The athlete is set as index now, instead of default numeric index (0-rows)
af = df.set_index('Athlete')

print(af.head())

# reset index
# Returns a dataframe with default (integer-based) index
# inplace = False by default

of = af.reset_index()
print(of.head())

# sort_index
# Allows all the items to be sorted by that index
# by default, inplace=False and ascending=True

af.sort_index(inplace=True)
print(af.head())


# DataFrame.loc[] / DataFrame.Series.loc[]
# A label-based indexer for selection by label
# loc raises a KeyError when items are not found

# df.loc['BOLT, Usain'] # raises keyError as df has integer based indexing
print (af.loc['BOLT, Usain'])


# DataFrame.iloc[]
# iloc[] is primarily integer position based (from 0 to length -1 of the axis)
# Allows traditional Pythonic slicing

print (df.iloc[1700]) # single entry

print (df.iloc[[123, 242, 179, 1500]]) # multiple entries

print (df.iloc[1:4])  # slicing
