mylist = [3, 7, 15, 2]

for whatever in mylist:
    print(whatever ** 2)

import datetime
now = datetime.datetime.now()

founded = {"Eric": 1943, "UCL": 1826, "Cambridge": 1209}

current_year = now.year

for thing in founded:
    print(thing, "is", current_year - founded[thing], "years old.")

for n in range(50):
    if n == 20:
        break
    if n % 2 == 0:
        continue
    print(n)
