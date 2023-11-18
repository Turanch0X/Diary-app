import calendar, datetime
from tkinter import *

days = []
# date = datetime.datetime #for the Дневник.py file
now = datetime.datetime.today()
year = now.year
month = now.month

# this_month_dates = []

def fill(info_label):
    info_label['text'] = calendar.month_name[month]+', '+str(year)
    month_days = calendar.monthrange(year,month)[1]
    if month==1:
        back_month_days = calendar.monthrange(year-1,12)[1]
    else:
        back_month_days = calendar.monthrange(year,month-1)[1]
    week_day = calendar.monthrange(year,month)[0]

    for n in range(month_days):
        days[n + week_day]['text'] = n+1
        days[n + week_day]['fg'] = 'blue' #without -1
        if year==now.year and month==now.month and n==now.day: #attention
            days[n+week_day-1]['bg'] = 'green' #formula
            days[n+week_day]['bg'] = 'lightgray'
        else:
            days[n+week_day]['bg'] = 'lightgray'
        
        current_date = datetime.date(year, month, n+1)
        if current_date.weekday() >= 5:
            days[n + week_day]['fg'] = 'red'  # Change font color for weekends
            days[n + week_day]['bg'] = 'lightgray'  # Change background color for weekends
    
    for n in range(week_day):
        days[week_day-n-1]['text'] = back_month_days-n
        days[week_day-n-1]['fg'] = 'indigo'
        days[week_day-n-1]['bg'] = 'darkgray'

    for n in range(6*7 - month_days - week_day):
        day_index = week_day + month_days + n
        days[day_index]['text'] = n+1
        days[day_index]['fg'] = 'indigo'
        days[day_index]['bg'] = 'darkgray'

    # for day in days:
    #     if day['bg'] == 'lightgray' or day['bg'] == 'green':
    #         number = day['text']
    #         this_month_dates.append(number)
        
    # print(this_month_dates)
            

def back():
    global month,year
    month-=1
    if month==0:
        month=12
        year+=-1

def next():
    global month,year
    month+=1
    if month==13:
        month=1
        year+=1