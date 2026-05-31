import datetime

print()
print(datetime.date(2026,5,31))

print()
print(datetime.datetime.today())

print()
print(datetime.datetime.today().weekday()) # 0 is monday and 6 is sunday

print()
print(datetime.timedelta(days=7))

print()
print(datetime.datetime.now() + datetime.timedelta(days=7))