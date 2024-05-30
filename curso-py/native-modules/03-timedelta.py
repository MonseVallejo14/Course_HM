from datetime import datetime, timedelta

date1 = datetime(2024, 1, 1) + timedelta(weeks=1)
date2 = datetime(2024, 2, 1)

delta = date2 - date1
print(delta)
print("days", delta.days)
print("seconds", delta.seconds)
print("microseconds", delta.microseconds)
print("total_seconds()", delta.total_seconds())
