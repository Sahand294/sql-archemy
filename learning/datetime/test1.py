from datetime import date,time,datetime,timedelta
dates = datetime.now()
am_or_pm = ''
n = time(3,16,0)
if int(dates.strftime('%H')) > 12:
    t = str(int(dates.strftime('%H')) - 12)
    am_or_pm = 'pm'
else:
    t = int(dates.strftime('%H'))
    am_or_pm = 'am'
future_date = dates + timedelta(days=5)
print(dates.strftime(f'date %Y:%b:%d time {t}:%M:%S {am_or_pm}'))