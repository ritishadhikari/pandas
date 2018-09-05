import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\aapl.csv',parse_dates=['Date'],index_col='Date')
print("The Original DataFrame DF1 Looks Like :\n",df1,"\n")
print("Index of DataFrame DF1 is \n", df1.index, "\n")
print("Stock Price for a particular Month:\n", df1['2017-06'],"\n")
print("Closing Stock Price for a particular Month:\n", df1['2017-06']['Close'],"\n")
print("Average Volume Traded for a particular Month:\n", df1['2017-06']['Volume'].mean(),"\n")
print("Finding The Details from the Dataframe over a Range of Dates :\n",df1["2017-07-02":"2017-06-25"],"\n")

df2 = df1['High'].resample('M').mean()
print("The Resampled Monthly DataFrame DF2 for High Price looks like :\n", df2,"\n")

df3 = df1.reset_index()
#print(type(df3['Date'][0]))
df4 = df3.pivot_table(index=pd.Grouper(key='Date',freq='M'),values='High',aggfunc='mean')
print("The Resampled Monthly DataFrame DF4 through Grouper looks like :\n", df4,"\n")

