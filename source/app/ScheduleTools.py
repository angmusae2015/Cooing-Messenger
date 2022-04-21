import json
from datetime import datetime, date

series_path = "../data/Schedule.json"
with open(series_path) as f:
    schedule = json.load(f)


def get_schedule_in_range(start: date, end: date):
    sch_in_range = [schedule[t_num] for t_num in schedule if date_filter(start, end, schedule[t_num])]

    return sch_in_range


def date_filter(start: date, end: date, sch: dict):
    target = datetime.strptime(sch['date'], '%Y-%m-%d').date()

    return (target >= start) and (target <= end)


def get_schedule_by_num(t_num: str):
    return schedule[t_num.replace('-', '')]


def get_tracking_num(sch: dict):
    index = list(schedule.values()).index(sch)

    return list(schedule.keys())[index]