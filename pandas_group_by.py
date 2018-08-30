import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_by_cities.csv', index_col='day')
print("The original DataFrame Looks like :\n",df1,"\n")

df2 = df1.groupby('city')
print("Group By Data Frame looks like :\n ",df2,"\n")

print("Printing the Groupby Dataframe : \n")
for city, city_df in df2:
    print(city)
    print(city_df,"\n")

print("Printing for a Specific City :\n")
print(df2.get_group('paris'),"\n")

print("Printing the Maximum Value from a DataFrame :\n ")
print(df2.max(),"\n")

print("Printing the Mean Value from a DataFrame :\n ")
print(df2.mean(),"\n")

print(df2.plot())
plt.show()