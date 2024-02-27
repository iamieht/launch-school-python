# What is the difference between the year attribute and the isocalendar method?
from datetime import date

today = date.today()

today_year = today.year
print(today_year)
iso_year = today.isocalendar()[0]
print(iso_year)

# isocalendar method returns a 3-element tuple (year, week, weekday)
# year returns the year of that date
