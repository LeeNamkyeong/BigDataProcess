#!/usr/bin/python3
import datetime

birth_date = datetime.date(1994, 5, 5)
current_date = datetime.date(2022,10, 17)

lived = current_date - birth_date
print ( f"{lived.days} days")

