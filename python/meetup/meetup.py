from datetime import date
import calendar
import re


class MeetupDayException(Exception):
    def __init__(self, msg):
        self.msg = msg


days_of_week = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


# Numbers with "teenth" at the end
teenth_number = {13, 14, 15, 16, 17, 18, 19}


def weekdays(year, month, day_of_week):
    """ Returns dates of the specified weekday for the given year and month """

    _, number_of_days = calendar.monthrange(year, month)

    return [
        date(year, month, day)
        for day in range(1, number_of_days + 1)
        if calendar.weekday(year, month, day) == days_of_week[day_of_week]
    ]


def meetup(year, month, week, day_of_week):
    if week == "last":
        return weekdays(year, month, day_of_week)[-1]
    elif week == "teenth":
        days = [d.day for d in weekdays(year, month, day_of_week)]
        # Assume there is only one element left in the intersection and return it
        day = teenth_number.intersection(set(days)).pop()
        return date(year, month, day)
    elif re.match(r"\d+\w{2}", week):
        number = int(re.match(r"(\d+)\w{2}", week).group(1))
        dates = weekdays(year, month, day_of_week)

        print(len(dates), number)
        if number > len(dates):
            raise MeetupDayException(f"There is no {week} {day_of_week} in this month!")

        return dates[number - 1]
