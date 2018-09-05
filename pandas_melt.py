import pandas as pd

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_melt.csv')
print("The DataFrame DF1 looks like :\n", df1, "\n")

df2 = df1.melt(id_vars='day',value_vars=['chicago','chennai','berlin'],var_name='City',value_name='Temperature')
print("The Melt DataFrame DF2 looks like :\n", df2, "\n")

df3 = df2[df2['City']=='chennai']
print("DataFrame DF3 giving results for Chennai is :\n ", df3,"\n")