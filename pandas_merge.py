import pandas as pd


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
},index=[0,1,2])

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
},index=[1,0,2])

df3 = pd.concat([df1,df2],axis=1)
print("The Concatenated DataFrame DF3 Looks Like :\n",df3,"\n")

df4 = pd.merge(left=df1,right=df2,on='city')
print("The Merged Dataframe DF4 looks like :\n", df4,"\n")


df5 = pd.DataFrame({
    "city": ["new york","chicago","orlando",'baltimore'],
    "temperature": [21,14,35,32]})

df6 = pd.DataFrame({
    "city": ["chicago","new york","san fransisco"],
    "humidity": [65,68,75]})

df7 =pd.merge(left=df5,right=df6,on='city')
print("The Updated DataFrame DF7 looks like :\n", df7,"\n")

df8 =pd.merge(left=df5,right=df6,on='city',how='outer',indicator=True)
print("The Updated Outer Join DataFrame DF8 looks like :\n", df8,"\n")

df9 =pd.merge(left=df5,right=df6,on='city',how='left')
print("The Updated Left Join DataFrame DF9 looks like :\n", df9,"\n")

df10 =pd.merge(left=df5,right=df6,on='city',how='right')
print("The Updated Right Join DataFrame DF10 looks like :\n", df10,"\n")

df11 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df12 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})

df13 = pd.merge(left=df11,right=df12,on='city')
print("The Merged DataFrame DF13 Looks like :\n",df13,"\n")

df14 = pd.merge(left=df11,right=df12,on='city',suffixes=('_left','_right'))
print("The Merged DataFrame DF14 Looks like :\n",df14,"\n")

###df14.to_excel(r'C:\Users\ritis\PycharmProjects\CSV Files\Merged.xlsx',sheet_name='Merged Data',index=False,startrow=0,startcol=0)