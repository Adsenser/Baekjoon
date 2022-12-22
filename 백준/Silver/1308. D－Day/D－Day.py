import datetime

this_year,this_month,this_day = map(int,input().split())
d_year,d_month,d_day = map(int,input().split())

today = datetime.datetime(this_year,this_month,this_day)
target_day = datetime.datetime(d_year,d_month,d_day)

dday=target_day - today
if dday.days >=365243:
  print("gg")
else:
  print("D-"+str(dday.days))