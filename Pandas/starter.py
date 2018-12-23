import pandas as pd

pd.show_versions() # show pandas as well as dependencies versions
pd.show_versions(as_json=True)

print (pd.__version__)


# dataframes is a 2D array 



# series is a 1D array of indexed data
# pandas support both index and label based indexing


# accessing a single series
# df['column_name'] or df["column_name"] or df.column_name 
# dot notation won't work if there is a space in the column name

# accessing multiple series
# df[['column_name1', 'column_name2']]


# type(DataFrame)  Output : pandas.core.frame.DataFrame

# type(DataFrame.SeriesName)  Output : pandas.core.series.Series


df = pd.read_csv('olympics.csv', skiprows=4) # skip the first 4 rows

print (df.head())

print(df['City'])

print(type(df['City'])) # series

print(type(df[['City', 'Edition', 'Athlete']])) # dataFrame

print(df[['City', 'Edition', 'Athlete']].head())
