import pandas as pd

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather.csv')
print("The DataFrame df1 Looks like :\n",df1,"\n")

df2 = df1.pivot(index='date',columns='city')
print("The Pivot DataFrame df2 looks like \n",df2,"\n")

df3 = df1.pivot(index='date',columns='city', values='humidity')
print("The Pivot DataFrame df3 with only values looks like \n",df3,"\n")

df4 = df1.pivot(index='city',columns='date')
print("The Pivot DataFrame df4 looks like \n",df4,"\n")

df5 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather2.csv')
print("The DataFrame df5 Looks like :\n",df5,"\n")

df6 = df5.pivot_table(index='city',columns='date')
print("The Pivot DataFrame df6 looks like \n",df6,"\n")

df7 = df5.pivot_table(index='city',columns='date',aggfunc='mean')
print("The Pivot DataFrame df7 with aggfunc looks like \n",df7,"\n")

df8 = df5.pivot_table(index='city',columns='date',aggfunc='mean',margins=True)
print("The Pivot DataFrame df7 with aggfunc and margins looks like \n",df8,"\n")

df9 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather3.csv',parse_dates=['date'])
#df9['date'] = pd.to_datetime(df9['date']) #Converting the date column into timestamp format if parse_dates function is not used before hand
print("The DataFrame df9 Looks like :\n",df9,"\n")

df10 = df9.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')
print("The Pivot DataFrame df10 with grouper looks like \n",df10,"\n")