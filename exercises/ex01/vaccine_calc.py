"""A vaccination calculator."""

__author__ = "730409609"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop = int(input("population: "))
administered_doses = int(input("doses administered: "))
doses_per_day = int(input("doses per day: "))
target_percent = int(input("target percent vaccinated: "))

doses_left = round(pop*target_percent/100*2 - administered_doses)
number_of_days = round(doses_left/doses_per_day)
days_till_target_percent: timedelta = timedelta(number_of_days)
from datetime import datetime, timedelta
today: datetime = datetime.today()
future: datetime = today + days_till_target_percent

print("We will reach " + str(target_percent) + "% vaccination in " + str(number_of_days) + " days, which falls on " + str(future.strftime("%B %d, %Y")) + ".")
