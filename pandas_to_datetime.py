import pandas as pd

dates1 = ['2017-01-05 02:30:00 PM', 'Jan 5, 2017 14:30:00']
dates_to_date_time1 = pd.to_datetime(dates1)
print("The Date Time Converted Data Set Looks Like :\n", dates_to_date_time1, "\n")

dates2 = ['08-02-2017']
dates_to_date_time2 = pd.to_datetime(dates2,dayfirst=True)
print("The Date Time Converted Data Set with Day first Looks Like :\n", dates_to_date_time2, "\n")

dates3 = ['2017$01$05']
dates_to_date_time3 = pd.to_datetime(arg=dates3,format='%Y$%m$%d')
print("The Date Time Converted Data Set with Custom Dates Looks Like :\n", dates_to_date_time3, "\n")

dates4 = ['2017-01-05', 'Jan 6, 2017', 'abc']
dates_to_date_time3 = pd.to_datetime(arg=dates4, errors='coerce')
print("The Date Time Converted Data Set with Error Handling Looks Like :\n", dates_to_date_time3, "\n")

t = 1536082005
epochtime = pd.to_datetime(arg=t,unit='s')
print("The Epoch Time so fetched from Seconds is :\n", epochtime, "\n")

convt = epochtime.view('int64')
print("The Converted Seconds since Epoch is :\n", convt, "\n")