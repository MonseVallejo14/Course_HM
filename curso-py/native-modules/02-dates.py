# import time

# print(time.time())

from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 2, 1)

now = datetime.now()
print(now)

dateStr = datetime.strptime("2024-01-03", "%Y-%m-%d")

print(now.strftime("%Y.%m.%d"))

print(date1 > date2)

print(
    date1.year,
    date1.month,
    date1.day,
    date1.hour,
    date1.minute
)
