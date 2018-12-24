# How GroupBy Works

# Split the dataframe into groups based on some criteria
# Apply a function to each group independently
# Combine the results into a Dataframe

# Returns a groupby object

import pandas as pd

df = pd.read_csv('olympics.csv', skiprows=4)

# print (df.groupby('Edition'))  # returns a DataFrameGroupBy object

# print (list(df.groupby('Edition')))


# Iterate through a Group
# for key,group in DataFrame.groupby('column_name'):
#   print(key)
#    print(group)


#for group_key, group_value in df.groupby('Edition'):
    #print ("Key: ", group_key, type(group_key))
    #print ("Value: ", group_value, type(group_value))

# type(group_value) is dataFrame 



#GroupBy computations:
# GroupBy.size(), count(), first(), last(), min(), max(), head(), tail(), mean()

# agg() - multiple statistics in one calculation per group

print (df.groupby(['Edition', 'NOC', 'Medal']).agg(['min', 'max', 'count']))

print (df.groupby(['Edition', 'NOC', 'Medal']).agg({'Edition': ['min', 'max', 'count']}))

# this will give the first year , last year (he won the medal) and total number of medals Carl Lewis won.
oo = df[df.Athlete == 'LEWIS, Carl']
res = oo.groupby('Athlete').agg({'Edition': ['min', 'max', 'count']})
print(res)

# list of all the countries won the medal first time, last time and number of medals won
# Solution1
#df = df[['NOC', 'Edition']]
#print (df.groupby('NOC').agg({'Edition': ['min', 'max', 'count']}))

#Solution2
print(df.groupby('NOC').agg({'Edition': ['min', 'max', 'count']}))


# Which US athlete has won most models in every olympics? Include the athlete's discipline
gy = df[df.NOC == 'USA']
gy = gy.groupby(['Edition', 'Athlete', 'Medal']).size()
gy = gy.unstack('Medal', fill_value=0)
gy['Total'] = gy['Gold'] + gy['Silver'] + gy['Bronze']
gy.reset_index(inplace = True)
for year,group in gy.groupby('Edition'):
    print(group.sort_values('Total', ascending=False)[:1])

#print(gy)




