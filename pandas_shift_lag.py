import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\fb.csv',parse_dates=['Date'],index_col='Date')
print("The Original DataFrame DF1 looks like \n", df1, "\n")

df1['Next Day Price'] = df1.shift(periods=1)
print("The Data Frame DF1 now looks like :\n", df1, "\n")

df1['%change'] = ((df1['Next Day Price']-df1['Price'])/df1['Price'])*100
print("The Data Frame DF1 with percentage Change now looks like :\n", df1, "\n")

plt.plot(df1['%change'])

df2 = df1['Price']
print("The Index Type as of Present is :\n", df2.index, "\n")

idx = pd.date_range(start='2017-08-15', periods=len(df2),freq='B')
df2 = df2.reindex(idx)

print("The Updated Index Type is :\n", df2.index, "\n")

print("The Shifted Date w.r.t. the Price looks like \n",df2.tshift(periods=1),"\n")

#plt.show()