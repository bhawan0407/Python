import pandas as pd

df = pd.read_csv('olympics.csv', skiprows=4)

print(df.shape)  # (rows,cols)

print(df['City'].shape)

print(df[['City', 'Athlete']].shape)




# head() and tail()

# head(n) returns the first n rows
# tail(n) returns the last  n rows
# default value is 5 for both


print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))


# info() provides a summary of the dataframe 
# including number of entries, data type and 
# number of non-null entries for each series in dataframe

print(df.info())
