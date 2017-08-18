import datetime
import calendar

def meetup_day(year, month, weekday, occurance):
    
    new_calendar = calendar.Calendar()
    
    weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    occurances = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5}
    weektup = new_calendar.monthdays2calendar(year, month)
    cnt = 0
    
    flat_month = [item for l in weektup for item in l]
    iter_month = [flat_month.remove(item) for item in list(flat_month) if item[0] == 0]
    
    for days in flat_month:
        if occurance == 'teenth':
            if days[0] in range(13, 20) and days[1] == weekdays.get(weekday):
                day = days[0]
        elif occurance == 'last':
            dates_list = []
            if days[1] == weekdays.get(weekday):
                dates_list.append(days)
                day = dates_list[-1][0]
        else:
            if days[1] == weekdays.get(weekday):
                cnt += 1
            if cnt == occurances.get(occurance) and days[1] == weekdays.get(weekday):
                day = days[0]
           
    return datetime.date(year, month, day)