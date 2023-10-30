from datetime import datetime as dt


def prettify_date(date):
    date = dt.strptime(date, "%Y_%m_%d_%H_%M_%S")
    day = date.strftime("%d/%m/%Y")
    time = date.strftime("%I:%M %p")

    return [day, time]

def rating_avg(data:list) -> float:
    if len(data) == 0:
        return 0.0
    else:
        return sum([x[0] for x in data]) / len(data)