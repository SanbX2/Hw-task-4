from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Walter White", "birthday": "1990.03.10"},
    {"name": "Sherlock Holmes", "birthday": "1820.03.16"}
]

prepered_users = []
for user in users:
    birthdays = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    prepered_users.append({"name": user['name'], "birthday": birthdays})

def find_next_weekday(d: datetime, weekday: int):
    next_days = weekday - d.weekday()
    if next_days <= 0:
        next_days += 7
    
    return d + timedelta(days=next_days)


def get_upcoming_birthdays():
    days = 7
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in prepered_users:
        birthday_this_year = user['birthday'].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user['name'],
                "congratulation_date": congratulation_date_str
            })
    
    return upcoming_birthdays

print(get_upcoming_birthdays())