import re
import time

with open ('day4-input.txt', 'r') as data:
  myInput = data.read().splitlines()
  sortedIn = sorted(myInput, key=lambda dt: (time.strptime(dt[6:17], "%m-%d %H:%M")))
  for line in sortedIn:
    print(line)