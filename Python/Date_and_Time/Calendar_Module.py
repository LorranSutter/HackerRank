import calendar

weekdays = {
    0:'MONDAY',
    1:'TUESDAY',
    2:'WEDNESDAY',
    3:'THURSDAY',
    4:'FRIDAY',
    5:'SATURDAY',
    6:'SUNDAY'
    }

month, day, year = list(map(int,input().split()))
print(weekdays[calendar.weekday(year,month,day)]);
