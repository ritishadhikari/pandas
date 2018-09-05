import pandas as pd

df1 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\stocks_stack.xlsx',sheet_name='stock_price', header=[0,1])
print("The Dataframe DF1 looks like :\n", df1, "\n")

df2 = df1.stack(level=1)
print("The Stacked Dataframe DF2 looks like :\n", df2, "\n")

df3 = df1.stack(level=0)
print("The Stacked Dataframe DF3 looks like :\n", df3, "\n")

print("Looking for a Specific Company from a DataFrame :\n",df3['Facebook'],"\n")

print("Looking for a Specific Parameter from a DataFrame :\n",df2['Price to earnings ratio (P/E)'],"\n")

df4 = df2.unstack(level=-1)
print("The Unstacked DataFrame DF4 looks like :\n", df4, "\n")

'''df5 = df3.unstack(level=1)
print("The Unstacked DataFrame DF5 looks like :\n", df5, "\n")'''

df6 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\stocks_3_levels.xlsx',sheet_name='stock_price', header=[0,1,2])
print("The Original DataFrame DF6 looks like :\n", df6, "\n")

df7 = df6.stack(level=2)
print("The Stacked DataFrame DF7 looks like :\n", df7,"\n")

'''df8 = df7.unstack(0)
print("The Unstacked DataFrame DF8 looks like :\n", df8, "\n")'''

