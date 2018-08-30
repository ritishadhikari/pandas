import pandas as pd
import numpy as np
import re
df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_data_2.csv')
print("The Original Data Frame Looks like : \n", df1, '\n')

df2 = df1.replace(-99999, np.nan)
print("The Modified Data Frame DF1 is : \n",df2, "\n")

df3 = df1.replace({'temperature': -99999,
                   'windspeed': -99999,
                   'event': '0'}, np.nan)
print("The Updated DataFrame DF3 post replace function looks like :\n",df3, "\n")

df4 = df1.replace({-99999 : np.nan,
                   '0' : 'No Event'})
print("The Updated DataFrame DF34 post replace function looks like :\n",df4, "\n")

df5 = df1.replace({28 : '28 C',
                   2.0 : '2.0 mph'})
print("The ruined Dataframe DF5 looks like : \n", df5, "\n")

df6 = df5.replace({'temperature' : '[A-Za-z]',
                    'windspeed' : '[A-Za-z]',},'',regex=True)
print("The Updated DataFrame DF6 looks like : \n", df6,"\n")

df7 = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']})
print("The New DataFrame DF7 looks like :\n",df7,"\n")

df8 = df7.replace(['exceptional','average','good','poor'],[4,2,3,1])
print("The Updated Dataframe DF8 looks like \n",df8,"\n")