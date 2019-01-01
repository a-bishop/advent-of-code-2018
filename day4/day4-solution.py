import re
import time
from datetime import datetime
from collections import defaultdict
from collections import Counter

def most_mins_asleep():
  guardSleep = Counter()
  guardNum = re.compile(r'#(\d+)')
  for line in sortedIn:
    if '#' in line:
      currGuard = guardNum.search(line)[1]
    elif 'asleep' in line:
      startAsleep = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    elif 'wakes' in line:
      endSleep = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
      guardSleep[currGuard] += int((endSleep - startAsleep).seconds/60)
  for k,v in guardSleep.most_common(1):
    return k

def solve1():
  minCounter = 0
  mins = re.compile(r':(\d+)')
  guardAsleepMost = most_mins_asleep()
  countingMins = False
  for line in sortedIn:
    if guardAsleepMost in line:
      countingMins = True
    if(countingMins):
      if 'asleep' in line:
        startMins = int(mins.search(line)[1])
      elif 'wakes' in line:
        endMins = int(mins.search(line)[1])
        for i in range(startMins, endMins):
          minCounter += 1
      elif ('#' in line) & (guardAsleepMost not in line):
        countingMins = False
  print(int(minCounter) * int(guardAsleepMost))

with open ('day4-input.txt', 'r') as data:
  myInput = data.read().splitlines()
  sortedIn = sorted(myInput, key=lambda dt: (time.strptime(dt[6:17], "%m-%d %H:%M")))
  with open("day4-input-sorted.txt", "w") as f:
    for line in sortedIn:
      f.write(line + '\n')
  solve1()
