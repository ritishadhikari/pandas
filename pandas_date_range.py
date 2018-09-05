import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv(r"C:\Users\ritis\PycharmProjects\CSV Files\aapl_no_dates.csv")
print("The Original Data Frame Looks like :\n",df1,"\n")

dates = pd.date_range(start='6/1/2017',periods=len(df1),freq='B')
print("The Frequency of the Dates Column will look like \n", dates,"\n")

df1.set_index(dates,inplace=True)
print("The Updated Data Frame Looks like \n",df1, "\n")

df1['Close'].plot()

print("Finding The Details from the Dataframe over a Range of Dates :\n",df1["2017-06-01" : "2017-06-10"],"\n")

df2 = df1.asfreq(freq='D',method='pad')
print("The Updated Data Frame df2 with all the days are \n", df2, "\n")

s1 = pd.Series(np.random.randint(low=100,high=200,size=len(dates)),index=dates)
print("The Series that is built from random numbers and the daterange function is \n", s1,"\n")

#plt.show()