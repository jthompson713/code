import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 8, 9)
movie_release = datetime.date(2023, 8, 8)

days_away = (next_birthday - today).days
day_since = (today - movie_release).days

if today == next_birthday:
    print(f'{random_message} 🎂')
else:
    print(f'Your birthday is in {days_away} days! 🎉')

print(f'It has been {day_since} days since the movie was released! 🎥')