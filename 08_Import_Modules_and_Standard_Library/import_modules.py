from utils import find_index
from variables import my_name,arr
import random
from check_luck import change_my_luck
import datetime
import calendar
import antigravity # comic

print(random.__file__)

future = change_my_luck()
print(f'My name is {my_name} and my success rate is {(1/future["repetetion"])*100} % but luck is {future["luck"]}')
time = datetime.datetime.now()

print(calendar.month(time.year,time.month))
print(f"{calendar.day_name[time.weekday()]}, {time.date()} ")