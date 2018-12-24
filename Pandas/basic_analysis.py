import pandas as pd

df = pd.read_csv('olympics.csv', skiprows=4)

# value_counts() 
# returns all the unique values with their counts for each series in a dataframe
# method for series only

print (df.Edition.value_counts()) 

#print(df[['Edition', 'Gender']].value_counts()) # ERROR: dataframe has no attribute value_counts()

print(df.Gender.value_counts())
print(df.Gender.value_counts(ascending=True)) 

# also, dropna = True is by default in value_counts() method




# sort_values()
# sorts the values in a series along either axis
# can also be used on dataFrames as well
# by default inplace = False , ascending  = True

print (df['Athlete'].sort_values())

print(df.sort_values(by=['City', 'Athlete', 'Edition'])) # sort by the order they are mentioned


# Boolean Indexing
# boolen vectors can be used to filter data
# multiple conditions must be grouped together using brackets

print (df.Medal == 'Gold') # will give whole series of True and False values

print (df[df['Medal'] == 'Gold'])

print (df[(df['Medal'] == 'Gold') & (df['Gender'] == 'Women')])


# string handling
# available to every series using the str attribute
# Series.str() - access values of series as strings and apply several methods to it. 
# e.g.   Series.str.contains(), Series.str.startswith() , Series.str.isnumeric() and so on

print(df[df.Athlete.str.contains('Florence')])


# Question: In what events did Jesse Owens win the medal ?
jo = df[df.Athlete == 'OWENS, Jesse'][['Athlete', 'Event']]
print(jo.Event.value_counts())


# Question: Which country has won the most men's gold medals in singles badminton over the years?
# Sort the results alphabetically by player names
gbm = df[(df.Medal == 'Gold') & (df.Gender == 'Men') & (df.Sport == 'Badminton') & (df.Event == 'singles')]
gbm = gbm.sort_values(by=['Athlete'])
print(gbm['NOC'].value_counts())


# Question: Which three countries have won the most medals in recent years (from 1984 to 2008)?
rd = df[df.Edition >= 1984]
print (rd['NOC'].value_counts().head(3))


# Display the male gold medal winners for 100m Track and Field sprint event over the years.
# List the results starting with the most recent. Show the olympic city, edition, athlete and country they represent.


gwh = df[(df.Medal == 'Gold') & (df.Gender == 'Men') & (df.Event == '100m')]
gwh = gwh.sort_values(by=['Edition'], ascending = False)
print(gwh[['City', 'Edition', 'Athlete', 'NOC']])



