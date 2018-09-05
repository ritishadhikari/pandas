import pandas as pd

df1 = pd.read_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\survey.xls')
print("The Original DataFrame DF1 looks like :\n", df1, "\n")

df2 = pd.crosstab(index=df1['Nationality'],columns=df1['Handedness'],normalize=False,margins=True)
#Margins gives the total values
print("The Crosstab DataFrame df2 looks like :\n", df2, "\n")

df3 = pd.crosstab(index=df1['Sex'],columns=df1['Handedness'],normalize=False,margins=True)
print("The Crosstab DataFrame df3 looks like :\n", df3, "\n")

df4 = pd.crosstab(index=df1['Sex'],columns = ([df1['Nationality'],df1['Handedness']]),normalize='index')
print("The Crosstab DataFrame df4 looks like :\n", df4, "\n")

df5 = pd.crosstab(index=df1['Sex'],columns=df1['Handedness'],values=df1['Age'],aggfunc='mean')
print("The Crosstab DataFrame df5 which gives the average age looks like :\n", df5, "\n")
