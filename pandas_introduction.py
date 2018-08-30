import pandas as pd

df = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\nyc_weather.csv')
print("The Columns in the dataframe are : \n", df.columns,"\n")
print("The Raw Dataframe looks like : \n",df, "\n")
print("Max Temperature recorded : \n", df['Temperature'].max(),"\n")
print("Days when it rained :\n",df["EST"][df['Events']=='Rain'],"\n")
print("The Mean Windspeed was :\n", df['WindSpeedMPH'].mean(),"\n")
#Refining the df dataframe by replacing all the na values with 0 as a part of data munging activity
df.fillna(0,inplace=True)
print("The Updated windspeed post data munging is :\n", df['WindSpeedMPH'].mean(),"\n")