import pandas as pd
import numpy as np

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\stock_data.csv')
print("The Original DataFrame DF1 looks like : \n", df1,"\n")

df2 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\stock_data.csv',header=0,nrows=6, na_values=['not available','n.a.'])
#nrows - how many rows you want the dataframe to read , header - which row you want to take as the header
#na_values - convert any values into na values as per your needs
print("The filtered DataFrame DF2 Looks like : \n", df2, "\n")

df3 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\stock_data.csv',header=0,nrows=6,
                  na_values={'eps': ['not available'],
                             'price':['n.a.'],
                             'revenue':[-1],
                             ' people': ['n.a.']})
#In this step column by column na_values are getting selected
print("The filtered DataFrame DF3 Looks like : \n", df3, "\n")

#Exporting the df3 file to a csv file
df3.to_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\updated_stock_data.csv',columns=['tickers','revenue'],header=0)

df4 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\stock_data.xlsx', sheet_name="Sheet1")
print("The Dataframe extracted from Excel File Looks like : \n", df4, "\n")



def convert_people_column(cell):
    if cell == 'n.a.':
        return "Sam Walton"
    else:
        return cell

def convert_revenue_column(cell):
    if cell == -1:
        return np.nan
    else:
        return cell

def convert_price_column(cell):
    if cell == 'n.a.':
        return np.nan
    else:
        return cell

def convert_eps_column(cell):
    if cell == 'not available':
        return np.nan
    else:
        return cell

df5 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\stock_data.xlsx', sheet_name="Sheet1", converters=
      {'people':convert_people_column,
       'revenue' :convert_revenue_column,
       'price' :convert_price_column,
       'eps':convert_eps_column})
#converters - Converts certain Values into some other Values
print("The Updated DataFrame Looks like :\n",df5, "\n")

#Exporting the df5 file to a xlsx file
df5.to_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\Imported_Stocks.xlsx',sheet_name='Stocks',index=False,
             startrow=0,startcol=0)

df6 = pd.DataFrame( {'day' :['1/1/2017','1/2/2017','1/3/2017'],
                     'temperature' : [ 32,35,28],
                     'windspeed' :[6,7,2],
                     'event':['Rain','Sunny','Snow']})

#writing two dataframes into one excel sheet
with pd.ExcelWriter('Stocks_Weather.xlsx') as writer :
    df5.to_excel(writer, sheet_name='Stocks')
    df6.to_excel(writer,sheet_name='Weather')

