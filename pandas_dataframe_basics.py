import pandas as pd

df = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_data.csv')
print("The Data Frame is : \n", df ,"\n")
print("The shape of the DataFrame is :\n ", df.shape, "\n")
print("The intial rows of the DataFrame is :\n ", df.head(), "\n")
print("The last rows of the DataFrame is :\n ", df.tail(), "\n")
print("Printing from the second till the last row :\n ",df[2:], "\n")
print("The Columns in the dataframe is :\n", df.columns,"\n")
print("Type of the Columns :\n", type(df['day']),"\n")
print("Printing more than two columns :\n", df[['temperature','windspeed']],"\n")
print("Statistics of the Data Frame :,\n",df.describe(),"\n")
print("Dataframe where temperature is greater than equal to 32 :\n",df[df['temperature']>=32] ,"\n")
print("Print Day and Event in Dataframe where temperature maximum :\n",df[['day','event']][df['temperature']==df['temperature'].max()])
print("Printing the Default Index Value : \n", df.index,"\n")
#Changing the Index to day
df.set_index('day',inplace=True)
print("The updated Dataframe with New Index Looks like :\n", df, "\n")
print("Printing a Particular Row through the loc function : \n", df.loc['1/5/2017'],"\n")
print("Printing a Particular 3rd Row through the iloc function : \n", df.iloc[3],"\n")
#Resetting the Index
df.reset_index(inplace=True)
print("The Original DataFrame is now back : \n",df,"\n")