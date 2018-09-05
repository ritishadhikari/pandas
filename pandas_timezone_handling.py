import pandas as pd
from pytz import all_timezones

print("All the Timezones are :\n ",all_timezones, "\n")
df1 = pd.read_csv(r"C:\Users\ritis\PycharmProjects\CSV Files\msft.csv",header=1,index_col='Date Time',parse_dates=['Date Time'])
print("The Original DataFrame Looks Like :\n",df1,"\n")
print("The DateTime property for this Data Frame is : \n", df1.index)

df_us = df1.tz_localize(tz='US/Eastern')
print("The Updated DataFrame for US Eastern Time Zone Looks Like :\n",df_us,"\n")

df_ber = df_us.tz_convert(tz='Europe/Berlin')
print("The Updated DataFrame for Berlin Time Zone Looks Like :\n",df_ber,"\n")

df_cal = df_ber.tz_convert(tz='Asia/Calcutta')
print("The Updated DataFrame for Calcutta Time Zone Looks Like :\n",df_cal,"\n")

rng = pd.date_range(start='2018-09-01 09:00:00',periods=10,freq='30min')
s1 = pd.Series(range(10),index=rng)
print ("The Original Series is: \n", s1, "\n")

s2 = s1.tz_localize(tz= 'Europe/Berlin')
print("The Berlin Series looks like :\n ", s2, "\n")

s3 = s1.tz_localize(tz='Asia/Calcutta')
print("The Calcutta Series looks like :\n ", s3, "\n")

print("The Activity Count is :\n", s2+s3, "\n")