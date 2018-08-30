import pandas as pd

#Read from CSV
df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_data1.csv')
print("The Data Frame extracted from CSV looks like : \n ", df1, "\n")

#Read from EXCEL
df2 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\weather_data1.xlsx',sheet_name='Sheet1')
print("The Data Frame extracted from Excel looks like : \n ", df2, "\n")

#Dataframe from Python Dictionary
df3 = pd.DataFrame( {'day' :['1/1/2017','1/2/2017','1/3/2017'],
                     'temperature' : [ 32,35,28],
                     'windspeed' :[6,7,2],
                     'event':['Rain','Sunny','Snow']})
print("The DataFrame from a Dictionary looks like : \n ",df3, "\n")

#DataFrame from Tuples List
df4 = pd.DataFrame([('1/1/2017',32,6,'Rain'),('1/2/2017',35,7,'Sunny'),('1/3/2017',28,2,'Snow')],columns=['day','temperature','windspeed','event'])
print("The DataFrame from a List Looks like : \n", df4, "\n")