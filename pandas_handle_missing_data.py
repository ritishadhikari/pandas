import pandas as pd

df1 = pd.read_csv(r"C:\Users\ritis\PycharmProjects\CSV Files\weather_data_1.csv")
print("The Data Frame DF1 Looks Like :\n",df1,"\n")
print("Type of Day Column is :\n", type(df1['day'][0]),"\n")

df2 = pd.read_csv(r"C:\Users\ritis\PycharmProjects\CSV Files\weather_data_1.csv", parse_dates=['day'])
print("Type of Day Column now is :\n", type(df2['day'][0]),"\n")
df2.set_index('day',inplace=True)
print("The Updated Data Frame DF2 looks like :\n",df2,'\n')
row, column = df2.shape

df3 = df2.fillna(0)
#fillna converts the nan data into some meaningful value as per the user's needs
print("The Updated Dataframe DF3 Looks like \n",df3,"\n")

df4 = df2.fillna ({'temperature': 0,
                   'windspeed' : 0,
                   'event' : 'no event'})
print("The Updated Dataframe DF4 looks like : \n",df4,"\n")

df5 = df2.fillna(method='ffill', axis=0, limit=2)
print("The Updated Dataframe DF5 with forward fill data for NA values look like :\n",df5,"\n")

df6 = df2.interpolate(method='time',limit=2)
#interpolate gives the near correct values as per the input
print("The Updated Dataframe DF6 with interpolated data for NA values look like :\n",df6,"\n")

df7 = df2.dropna(how='any')
#choose between any or all
print("The Updated Dataframe DF7 with all the dropped rows look like : \n ",df7, "\n")

df8 = df2.dropna(thresh=column)
#thresh gives the rows with that many non nan values. It means tolerance level of na value = column - thresh
print("The Updated Dataframe D8 which gives the rows as per our wish of na value filtering looks like : \n", df8, "\n")


dt = pd.date_range(start='01-01-2017',end='01-11-2017')
idx = pd.DatetimeIndex(dt) #this line is optional
df9 = df2.reindex(idx)
print("The Data Frame with the entire dates looks like :\n",df9,"\n")
print(type(df9.index))