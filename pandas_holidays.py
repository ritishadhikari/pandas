import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas.tseries.holiday import AbstractHolidayCalendar
from pandas.tseries.holiday import Holiday
from pandas.tseries.holiday import nearest_workday

df1 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\aapl_no_dates_holidays.csv')
print("The Original DataFrame looks like \n",df1,"\n")

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())

dates1 = pd.date_range(start='2017-07-01',periods=len(df1),freq=usb)
print("The Dates Column dates1 would look like \n",dates1,"\n")

df1.set_index(keys=dates1,inplace=True)
print("The Updated Data Frame DF1 for any US Calendar Holiday Looks like :\n",df1,"\n")

###########################################################################################
df2 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\aapl_no_dates_holidays.csv')
print("The Original DataFrame DF2 looks like \n",df2,"\n")

class myBirthdayCalendar(AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/
       snow-dismissal-procedures/federal-holidays/
    """
    rules = [
        Holiday('Ritish"s Birthday', month=7, day=6) #observance=nearest_workday),
    ]

myc = CustomBusinessDay(calendar=myBirthdayCalendar())

dates2 = pd.date_range(start='2017-07-01',periods=len(df2),freq=myc)
print("The Dates Column dates2 would look like \n",dates2,"\n")

df2.set_index(keys=dates2,inplace=True)
print("The Updated Data Frame DF2 for any specific holiday Looks like :\n",df2,"\n")

###########################################################################################
df3 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\aapl_no_dates_holidays.csv')
print("The Original DataFrame DF3 looks like \n",df3,"\n")

class Nearestweekdaycalendar(AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/
       snow-dismissal-procedures/federal-holidays/
    """
    rules = [
        Holiday('Nearest Workday', month=7, day=8, observance=nearest_workday)
    ]

nwc = CustomBusinessDay(calendar=Nearestweekdaycalendar())

dates3 = pd.date_range(start='2017-07-01',periods=len(df3),freq=nwc)
print("The Dates Column dates2 would look like \n",dates3,"\n")

df3.set_index(keys=dates3,inplace=True)
print("The Updated Data Frame DF3 for Nearest WorkDay Looks like :\n",df3,"\n")

###########################################################################################
df4 = pd.read_csv(r'C:\Users\ritis\PycharmProjects\CSV Files\aapl_no_dates_holidays.csv')
print("The Original DataFrame DF4 looks like \n",df4,"\n")




egc = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu',holidays=['2017-07-04'])

dates4 = pd.date_range(start='2017-07-01',periods=len(df4),freq=egc)
print("The Dates Column dates2 would look like \n",dates4,"\n")

df4.set_index(keys=dates3,inplace=True)
print("The Updated Data Frame df4 for Egypt Calendar with US Independence Day Holiday Looks like :\n",df4,"\n")