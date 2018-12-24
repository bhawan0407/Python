import pandas as pd

df = pd.read_csv('olympics.csv', skiprows=4)

import matplotlib.pyplot as plt
import pylab

# plot the different sports in the first olympics using different graphs

fs = df[df.Edition == 1896]

fs['Sport'].value_counts().plot()  # default is line plot
pylab.show()

fs['Sport'].value_counts().plot(kind='bar')  # bar plot
pylab.show()

fs['Sport'].value_counts().plot(kind='barh')  # horizontal bar plot
pylab.show()

fs['Sport'].value_counts().plot(kind='pie')  # pie chart
pylab.show()


# you can specify different colors also in the plots you want to see

fs['Sport'].value_counts().plot(color='green')  # default is line plot
pylab.show()

fs['Sport'].value_counts().plot(kind='bar', color='blue')  # bar plot
pylab.show()

fs['Sport'].value_counts().plot(kind='barh')  # horizontal bar plot
pylab.show()

fs['Sport'].value_counts().plot(kind='pie')  # pie chart , no color parameter for this.
pylab.show()


# figure size is a tuple in which we can specify width and height (in inches)
# e.g. plot(figsize(5,5))

fs['Sport'].value_counts().plot(kind='bar', color='maroon', figsize = (2,3))
pylab.show()


