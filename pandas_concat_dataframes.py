import pandas as pd

india_weather = pd.DataFrame({'city' : ['Mumbai','Delhi','Bangalore'],
                 'temperature' :[32,45,30],
                 'humidity':[80,60,78]})
print("India Weather DataFrame Looks Like :\n", india_weather,"\n")

us_weather = pd.DataFrame({'city' : ['New York','Chicago','Orlando'],
                 'temperature' :[21,14,35],
                 'humidity':[68,65,75]})
print("US Weather DataFrame Looks Like :\n", us_weather,"\n")

df1 = pd.concat([india_weather,us_weather],axis=0,ignore_index=True)
print("The Concatenated DataFrame clubbing the index looks like :\n", df1, "\n")

df2 = pd.concat([india_weather,us_weather],keys=['India','USA'])
print("The Concatenated DataFrame with the keys looks like :\n", df2, "\n")
print("Searching for a specific Part of the Dataframe through the loc function :\n",df2.loc['India'],"\n")


india_weather_2 = pd.DataFrame({'city' : ['Mumbai','Delhi','Bangalore'],
                 'temperature' :[32,45,30],
                 'humidity':[80,60,78]},index=[0,1,2])
india_windspeed = pd.DataFrame({'city' : ['Delhi','Mumbai'],
                 'windspeed' :[32,45]},index=[1,0])

df3 = pd.concat([india_weather_2,india_windspeed],axis=1)
print("The Concatenated DataFrame in column wise looks like :\n", df3,"\n")

series = pd.Series(['Humid','Dry','Rain'],name='Event')
df4 = pd.concat([india_weather_2,series],axis=1)
print("The Concatenated DataFrame, i.e., a dataframe and a series in column wise looks like :\n", df4,"\n")